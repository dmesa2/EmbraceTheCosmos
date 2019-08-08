import pygame
import os
from pygame.locals import *
from gamestate import *
import json
from collections import defaultdict

class Hand(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw_rect(self, screen):
        for s in self.sprites():
            s.show_box(screen, WHITE)

    def draw(self, screen):
        for card in self.sprites():
            screen.blit(card.image, card.rect)
            if card.highlight:
                card.show_box(screen, CYAN, 2)

    def ddraw(self, screen, position, power):
        for card in self.sprites():
            screen.blit(card.image, card.rect)
            if card.cost <= power and card.rect.collidepoint(position):
                card.show_box(screen, CYAN, 2)

    def position_hand(self):
        ncards = len(self.sprites())
        total_width = CARD_WIDTH * ncards
        x = (SCREEN_WIDTH  - total_width) / 2
        y = SCREEN_HEIGHT - CARD_HEIGHT
        for sp in self.sprites():
            sp.pos = [x, y]
            x += CARD_WIDTH
            sp.update()

    def get_area(self):
        width = SCREEN_WIDTH * 4 / 6
        top = SCREEN_HEIGHT - CARD_HEIGHT
        left = (SCREEN_WIDTH  - width) / 2
        offset_x = SCREEN_WIDTH * 0.1
        offset_y = SCREEN_HEIGHT * 0.1
        return pygame.Rect((left - offset_x, top - offset_y, width + 2 * offset_x, CARD_HEIGHT + CARD_HEIGHT + offset_y ))

    def mincost(self):
        return min(self.sprites(), key=lambda sp : sp.cost).cost

    def buy_card(self, player, pos):
        for card in self.sprites():
            if card.rect.collidepoint(pos):
                if card.price <= player.credits:
                    player.credits -= card.price
                    self.remove(card)
                    player.all_cards.append(card)


class Card(pygame.sprite.Sprite):
    def __init__(self, x, y, name, ctype, cost, pclass, damage, shield, price, image_path=None, image=None):
        super().__init__()
        pygame.font.init()
        font = pygame.font.Font(None, 16)
        if image_path:
            pth = os.path.join(CARD_PATH, image_path)
            self.image_path = image_path
            self.image = pygame.transform.scale(pygame.image.load(pth).convert(), (CARD_WIDTH, CARD_HEIGHT))
        else:
            self.image = image
        self.id = 0
        self.pos = [x, y]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.highlight = False
        # EFFECTS
        # Type: TARGET_ATTACK, AREA_ATTACK, BOOST, POWER
        self.ctype = ctype
        self.name = name
        # Power cost to ship
        self.cost = cost
        # Dictionary to hold alternate effects
        self.status_effect = dict()
        # Player Class e.g. fighter
        self.pclass = pclass
        self.damage = damage
        self.shield = shield
        self.price = price
        self.price_str = font.render("{} credits".format(self.price), 
                                        False, Color("gold"))

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)

    def show_box(self, screen, color, width=1):
        pygame.draw.rect(screen, color, self.rect, width)

    def copy(self):
        return Card(self.pos[0], self.pos[1], self.name,
                    self.ctype, self.cost, self.pclass, self.damage,
                    self.shield, self.price, image=self.image)

    def process_card(self, screen, player, enemy_group, assets):
        position = pygame.mouse.get_pos()
        if self.ctype == "TARGET_ATTACK" or self.ctype == "AREA_ATTACK":
            laser, l_rect = assets.laser_img, assets.laser_rect
            l_rect.midleft = player.rect.midright
            # Shoot laser
            for i in range(5):
                screen.blit(laser, l_rect)
                pygame.display.update()
                pygame.time.wait(50)
                pygame.draw.rect(screen, BLACK, l_rect)
                l_rect.x += 50

        if self.ctype == "TARGET_ATTACK":
            targeted = [sp for sp in enemy_group if sp.collision(position)]
            if targeted:
                enemy_group.process_attack(self, targeted[0])
        elif self.ctype == "BOOST":
            player.shield += self.shield
        elif self.ctype == "AREA_ATTACK":
            enemy_group.process_attack(self)
        player.hand.remove(self)
        player.graveyard.append(self)

def read_card(card):
    return Card(0, 0, card['name'], card['type'], card['cost'],
             card['class'], card['damage'], card['shield'], card['price'],
             image_path=card['image'])

def load_cards(fname):
    with open(fname, 'r') as f:
        cards = json.load(f)
    all_cards = defaultdict(list)
    for card in cards:
        all_cards[card['class']].append(read_card(card))
    return all_cards
