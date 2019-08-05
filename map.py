import pygame
import os
import random
import sys
import math

from pygame.locals import *
from gamestate import *
from battle import battle
from repair import repair
from shop import shop
from gameover import game_over

LAST = -1
FIRST = 1

ALPHA = 200

# Access levels
INACCESSIBLE = 0
ACCESSIBLE = 1
CURRENT_LOCATION = 2

def get_rand():
    # Gets a random numbers from an uneven distrubution
    nums = [2, 2, 2, 3, 3, 3, 4, 4, 5, 6]
    return random.choice(nums)

class Icon(pygame.sprite.Sprite):
    def __init__(self, image, shadow_image, type=None, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        self.image = image
        self.shadow_image = shadow_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.children = []

    def connect(self, screen):
        # draw connections between nodes
        [pygame.draw.line(screen, ORCHIRD, self.rect.midtop, child.rect.midbottom) for child in self.children]


    def draw(self, screen, access=False):
        if self.y < -50 or self.y > SCREEN_HEIGHT + 50:
            return
        if access:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.shadow_image, self.rect)
        self.connect(screen)

    def up(self):
        self.y += MAP_DELTA
        self.update()

    def down(self):
        self.y -= MAP_DELTA
        self.update()

    def collide(self, position):
        return self.bounding_rect.collidepoint(position)

    def copy(self):
        return Icon(self.image, self.shadow_image, self.type, self.x, self.y)

    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center

    def is_child(self, parent):
        return self in parent.children

class IconTree(pygame.sprite.Group):
    def __init__(self, images):
        super().__init__()
        # placeholder surface until actual images are filled in
        image = pygame.surface.Surface((1, 1))
        # start with 3-5 nodes for the player to start at
        starting_nodes = random.randint(3, 5)
        last_level = [Icon(image, image) for i in range(1, starting_nodes + 1)]
        self.root = Icon(image, image)
        self.root.children = last_level
        # holds node list for each level of the tree
        self.levels = [[self.root], last_level]

        while len(self.levels) < 14:
            new_level = [] # nodes that are being newly added
            '''
            Generate between 2 and 6 nodes for the next level
            Each node can have at most half of the previous nodes connecting to it.
            Only the last node connected
            '''
            new_level = [Icon(image, image) for _ in range(get_rand())] # random.randint(2, 6))]
            has_parent = [False for _ in range(len(new_level))]
            max_conn = math.ceil(len(last_level) / 2)
            start_idx = 0
            for parent in last_level:
                if max_conn <= 1:
                    new_conn = 1
                else:
                    new_conn = random.randint(1, max_conn)
                end = min(start_idx + new_conn, len(new_level))
                for i in range(start_idx, end):
                    parent.children.append(new_level[i])
                    has_parent[i] = True
                start_idx = min(start_idx + new_conn - 1, len(new_level) - 1)
            # Hook up oprhaned nodes
            for chld, parent in zip(new_level, has_parent):
                if not parent:
                    last_level[-1].children.append(chld)

            # Get ready to move onto next level
            self.levels.append(new_level)
            last_level = new_level
        '''
        Add final repair nodes.
        Before the boss players will have the option to repair.
        '''
        repair = []
        repair_nodes = min(4, len(self.levels[LAST]))
        last = 0
        if repair_nodes == len(self.levels[LAST]):
            nodes_per_repair = 1
        else:
            nodes_per_repair = len(self.levels[LAST]) // repair_nodes
        for i in range(repair_nodes):
            temp = Icon(*images['repair'])
            repair.append(temp)
            for parent in self.levels[LAST][i * nodes_per_repair : (i + 1) * nodes_per_repair]:
                parent.children.append(temp)
        for parent in self.levels[LAST][i * nodes_per_repair:]:
            parent.children.append(temp)
        self.levels.append(repair)
        ''' Add final boss node. '''
        boss = Icon(*images['boss'])
        for parent in self.levels[LAST]:
            parent.children.append(boss)
        self.levels.append([boss])
        '''
        Generate actual icons at each node positoin in each map
        Rest, Shop, Unknown, Minion
        '''
        total_encounters = sum([len(lvl) for lvl in self.levels[1:-2]])
        selections = ['unknown'] * int(total_encounters * 0.30) + \
                     ['minion'] * int(total_encounters * 0.40)
        random.shuffle(selections)
        for nodes in self.levels[1:3]:
            for node in nodes:
                node.type = selections.pop()
                node.image, node.shadow_image = images[node.type]
                node.update()
        selections += ['repair'] * int(total_encounters * .15) + \
                      ['shop'] * int(total_encounters * .15)
        rem_nodes = sum(len(lvl) for lvl in self.levels[3:-2])
        while len(selections) < rem_nodes:
            selections.append('minion')
        random.shuffle(selections)
        for nodes in self.levels[3:-2]:
            for node in nodes:
                node.type = selections.pop()
                node.image, node.shadow_image = images[node.type]
                node.update()

        # Add all newly created nodes to the group
        for l in self.levels:
            self.add(*l)
        # generate positions for each node based on the number of nodes per level
        self.position()

    def draw(self, screen):
        position = pygame.mouse.get_pos()
        for icon in self.sprites():
            if icon != self.root:
                icon.draw(screen)

    def position(self):
        '''
        Establishes positions of procedurally generated map icons.
        Only needs to be called directly after new map initialization.
        '''
        delta_y = 150
        y_coord = SCREEN_HEIGHT - 60
        # establish positions of current level, skip root level
        for current in self.levels[1:]:
            n = len(current)
            field = int(SCREEN_WIDTH * .9)
            delta_x = (field - n * 40) / (n  + 1)
            x_coord = delta_x + int(SCREEN_WIDTH *.1)
            for n in current:
                n.x = x_coord
                n.y = y_coord
                x_coord += delta_x + 40
            y_coord -= delta_y
        self.update()

    def scroll(self, screen, bg, legend, up, down, up_rect, down_rect):
        '''
        Enables scrolling of map with arrow icons at bottom right hand side.
        Will stop when the last row of icons display is going off the screen.
        '''
        while pygame.mouse.get_pressed()[MOUSE_ONE]:
            pygame.time.Clock().tick(40)
            screen.blit(bg, (0, 0))
            screen.blit(up, up_rect)
            screen.blit(down, down_rect)
            pos = pygame.mouse.get_pos()
            if down_rect.collidepoint(pos):
                self.down()
            elif up_rect.collidepoint(pos):
                self.up()
            self.draw(screen)
            screen.blit(legend, (580, 20))
            pygame.display.update()
            pygame.event.pump()

    def up(self):
        # Stop scrolling when last level is about to go off the bottom
        if self.levels[LAST][0].y >= SCREEN_HEIGHT:
            return
        for sp in self.sprites():
            sp.up()

    def down(self):
        # Stop scrolling when first level is about to go off the top
        if self.levels[FIRST][0].y <= 0:
            return
        for sp in self.sprites():
            sp.down()

class Map:
  def __init__(self):
     self.images = {}
     #Boss
     bi = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech-small.png').convert_alpha(), (70, 70))
     bi_shadow = bi.copy()
     bi_shadow.set_alpha(ALPHA)
     self.images['boss'] = (bi, bi_shadow)
     #Minions
     minion = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png').convert_alpha(), (40, 40))
     minion_shadow = minion.copy()
     minion_shadow.set_alpha(ALPHA)
     self.images['minion'] = (minion, minion_shadow)
     #Stores
     store = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png').convert_alpha(), (40, 40))
     store_shadow = store.copy()
     store_shadow.set_alpha(ALPHA)
     self.images['shop'] = (store, store_shadow)
     #Unknown
     unk = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png').convert_alpha(), (40, 40))
     unk_shadow = unk.copy()
     unk_shadow.set_alpha(ALPHA)
     self.images['unknown'] = (unk, unk_shadow)
     # Repair
     rep = pygame.transform.scale(pygame.image.load('assets/map_icons/auto-repair.png').convert_alpha(), (40, 40))
     rep_shadow = rep.copy()
     rep_shadow.set_alpha(ALPHA)
     self.images['repair'] = (rep, rep_shadow)

     # Background
     self.bg = pygame.transform.scale(pygame.image.load(os.path.join(BACKGROUND_PATH, "nebula/nebula09.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
     #Legend
     self.legend = pygame.transform.scale(pygame.image.load('assets/map_icons/Legend.png'), (200, 50))
     # Up/Down buttons
     self.up = pygame.transform.scale(pygame.image.load(os.path.join(ICON_PATH, "upgrade.png")), (ICON_SIZE, ICON_SIZE))
     self.down = pygame.transform.scale(pygame.image.load(os.path.join(ICON_PATH, "downgrade.png")), (ICON_SIZE, ICON_SIZE))
     self.down_rect = self.down.get_rect(bottomright=(SCREEN_WIDTH, SCREEN_HEIGHT))
     self.up_rect = self.up.get_rect(topright=self.down_rect.topleft)

  def main_map(self, screen, player, assets):
      sector_map = IconTree(self.images)
      sector_map.update()
      player_loc = sector_map.root
      alive = True
      while alive:
        screen.blit(self.bg, (0, 0))
        screen.blit(self.legend, (580, 20))
        screen.blit(self.up, self.up_rect)
        screen.blit(self.down, self.down_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            elif event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if self.up_rect.collidepoint(position) or self.down_rect.collidepoint(position):
                    sector_map.scroll(screen, self.bg, self.legend, self.up, self.down, self.up_rect, self.down_rect)
                for sp in sector_map.sprites():
                    if sp.is_child(player_loc) and sp.collide(position):
                        player_loc = sp
                        if sp.type == 'minion' or sp.type == 'unknown' or sp.type == 'boss':
                            alive = battle(screen, player, assets)
                        elif sp.type == 'repair':
                            repair(screen, player, assets)
                        elif sp.type == 'shop':
                            shop(screen, player, assets)
            if alive:
                sector_map.draw(screen)
                pygame.display.update()
        if player.current_health <= 0:
            game_over(screen)
