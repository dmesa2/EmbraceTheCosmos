import pygame
import os
import random
import sys

from pygame.locals import *
from gamestate import *
from battle import battle
from repair import repair
from shop import shop

LAST = -1
FIRST = 1

def get_rand():
    nums = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]
    return random.choice(nums)

def connect(screen, node):
    if not node:
        return
    for child in node.children:
        pygame.draw.line(screen, ORCHIRD, node.rect.midtop, child.rect.midbottom)
        connect(screen, child)

class Icon(pygame.sprite.Sprite):
    def __init__(self, image, lg_image, type=None, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        self.image = image
        self.lg_image = lg_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.lg_rect = self.lg_image.get_rect(center=self.rect.center)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.children = []

    def draw(self, screen, large=False):
        if large:
            screen.blit(self.lg_image, self.rect)
        else:
            screen.blit(self.image, self.lg_rect)

    def up(self):
        self.y += MAP_DELTA
        self.update()

    def down(self):
        self.y -= MAP_DELTA
        self.update()

    def collide(self, position):
        return self.bounding_rect.collidepoint(position)

    def copy(self):
        return Icon(self.image, self.lg_image, self.type, self.x, self.y)

    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.lg_rect = self.lg_image.get_rect(center=(self.x, self.y))
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center

class IconTree(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        image = pygame.surface.Surface((1, 1))
        total_encounters = 40
        starting_nodes = random.randint(3, 5)
        last_level = [Icon(image, image) for i in range(1, starting_nodes + 1)]
        n_nodes = starting_nodes
        self.root = Icon(image, image)
        self.root.children = last_level.copy()
        self.levels = [[self.root], last_level]
        while n_nodes < total_encounters:
            empty_nodes = []
            new_level = []
            for node in last_level:
                new_nodes = get_rand()
                n_nodes += new_nodes
                if new_nodes == 0:
                    if not new_level:
                        empty_nodes.append(node)
                    else:
                        node.children.append(new_level[-1])
                else:
                    for _ in range(new_nodes):
                        temp = Icon(image, image)
                        new_level.append(temp)
                        while empty_nodes:
                            empty_nodes.pop().children.append(temp)
                        node.children.append(temp)
            if not empty_nodes:
                self.levels.append(new_level)
                last_level = new_level
        for l in self.levels:
            self.add(*l)

    def draw(self, screen):
        position = pygame.mouse.get_pos()
        for icon in self.sprites():
            if icon != self.root:
                icon.draw(screen, icon.collide(position))

    def position(self, width, height):
        delta_y = 150
        y_coord = height - 60

        # establish positions of current level, skip root level
        for current in self.levels[1:]:
            n = len(current)
            field = int(width * .9)
            delta_x = (field - n * 40) / (n  + 1)
            x_coord = delta_x + int(width *.1)
            for n in current:
                n.x = x_coord
                n.y = y_coord
                x_coord += delta_x + 40
            y_coord -= delta_y
        self.update()

    def scroll(self, screen, bg, legend, up, down, up_rect, down_rect):
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
            self.connect(screen)
            self.draw(screen)
            screen.blit(legend, (580, 20))
            pygame.display.update()
            pygame.event.pump()

    def connect(self, screen):
        for child in self.root.children:
            connect(screen, child)

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
     bi = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech-small.png'), (70, 70))
     bi_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech.png'), (85, 85))
     self.images['boss'] = (bi, bi_lg)
     #Minions
     minion = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
     minion_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))
     self.images['minion'] = (minion, minion_lg)
     #Stores
     store = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40))
     store_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50))
     self.images['shop'] = (store, store_lg)
     #Unknown
     unk = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png'), (40, 40))
     unk_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty.png'), (50, 50))
     self.images['unknown'] = (unk, unk_lg)
     # Background
     self.bg = pygame.transform.scale(pygame.image.load(os.path.join(BACKGROUND_PATH, "nebula/nebula09.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
     #Legend
     self.legend = pygame.transform.scale(pygame.image.load('assets/map_icons/Legend.png'), (200, 50))
     # Up/Down buttons
     self.up = pygame.transform.scale(pygame.image.load(os.path.join(ICON_PATH, "upgrade.png")), (20, 20))
     self.down = pygame.transform.scale(pygame.image.load(os.path.join(ICON_PATH, "downgrade.png")), (20, 20))
     self.down_rect = self.down.get_rect(bottomright=(SCREEN_WIDTH, SCREEN_HEIGHT))
     self.up_rect = self.up.get_rect(topright=self.down_rect.topleft)

  def main_map(self, screen, player, assets):
      sector_map = IconTree()
      for sp in sector_map.sprites():
          sp.image, sp.lg_image = self.images['minion']
      sector_map.update()
      sector_map.position(SCREEN_WIDTH, SCREEN_HEIGHT)
      sector_map.update()
      while True:
        pygame.time.Clock().tick(40)
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
                    if sp.collide(position):
                        if sp.type == 'minion':
                            battle(screen, player, assets)
                        elif sp.type == 'unknown':
                            repair(screen, player, assets)
                        elif sp.type == 'shop':
                            shop(screen, player, assets)

            sector_map.connect(screen)
            sector_map.draw(screen)
            pygame.display.update()
