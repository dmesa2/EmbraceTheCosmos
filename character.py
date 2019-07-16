import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import sprite
import random
import cards
from gamestate import *

X = 0
Y = 1

class Enemy_Gr(sprite.Group):
    def __init__(self):
        super().__init__()

    def draw_rect(self, screen):
        for s in self.sprites():
            s.show_box(screen)
    def draw(self, screen):
        for sp in self.sprites():
            sp.draw(screen)

    def process_attack(self, card, target=None):
        if target:
            target.damage(card.damage)
        else:
            for sp in self.sprites():
                sp.damage(card.damage)
    def spawn(self):
         # change to dynamically create enemies
        enemy0 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship4/Ship4.png'), 15)
        enemy1 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship2/Ship2.png'), 15)
        enemy2 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship5/Ship5.png'), 10)
        self.add(enemy0, enemy1, enemy2)
class Character(sprite.Sprite):
    def __init__(self, image, max_health=40):
        super().__init__()
        self.image = pygame.image.load(image)
        self.pos = [0, 0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.health_bar = self.health_init()
        # stats
        self.max_health = max_health
        self.current_health = max_health
        self.shield = 0

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.health_init()

    def health_init(self):
        left, top, width, height = self.bounding_rect
        self.health_bar = pygame.Rect((left, top + height, width, 8))

    def collision(self, position):
        return self.bounding_rect.collidepoint(position)

    def rescale(self, w, h):
        self.image = pygame.transform.scale(self.image, (w, h))

    def rescale_factor(self, n):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * n, height * n))

    def move(self, x, y):
        self.pos = [x, y]
        self.update()

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def get_img(self):
        return self.image

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.bounding_rect, 1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        if self.max_health > 0:
            if self.shield:
                pygame.draw.rect(screen, BLUE, self.health_bar)
            else:
                pygame.draw.rect(screen, GRAY, self.health_bar)
                health = self.health_bar.copy()
                health.width *= self.current_health / self.max_health
                pygame.draw.rect(screen, RED, health)


class Player(Character):
    def __init__(self, image, health):
        super().__init__(image, health)
        self.max_handsize = 3
        self.all_cards = []
        # battle hands
        self.hand = cards.Hand()
        self.graveyard = []
        self.deck = []
        self.in_play = []

    def draw_hand(self):
        for _ in range(self.max_handsize):
            # If deck is empty reshuffle graveyard into deck before drawing cards
            if not self.deck:
                random.shuffle(self.graveyard)
                self.deck = self.graveyard.copy()
                self.graveyard = []
            c = self.deck.pop()
            self.hand.add(c)

    def reset_decks(self):
        self.hand.empty()
        self.deck = self.all_cards.copy()
        random.shuffle(self.deck)
        self.graveyard = []
        self.in_play = []

    def end_turn(self, board):
        for card in self.hand:
            self.graveyard.append(card)
            card.remove(self.hand)
        self.draw_hand()
        self.hand.position_hand()

class Enemy(Character):
    def __init__(self, image, health, shield, atk_pattern):
        super().__init__(image, health)
        self.shield = shield
        self.attacks = atk_pattern
        self.attack_idx = 0

    def damage(self, ndmg):
        if self.shield:
            if self.shield > ndmg:
                self.shield -= ndmg
            else:
                ndmg -= self.shield
                self.shield = 0
                self.current_health -= ndmg
        else:
            self.current_health -= ndmg
        if self.current_health <= 0:
            self.remove(self.groups())

class Target(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Misc/red_target.png"), (24, 24))
        self.attack_img = pygame.transform.scale(pygame.image.load("assets/Misc/green_target.png"), (24, 24))
        self.boost_img = pygame.transform.scale(pygame.image.load("assets/Misc/blue_target.png"), (24, 24))
        self.rect = self.image.get_rect()

    def update(self, position):
        self.rect = self.image.get_rect(topleft=position)

    def get_img(self):
        return self.image

    def get_atk(self):
        return self.attack_img

    def get_bst(self):
        return self.boost_img

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)
