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

class Character(sprite.Sprite):
    def __init__(self, image, max_health=40, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image)
        self.pos = [x, y]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.health_bar = self.health_init()
        # stats
        self.max_health = max_health
        self.current_health = max_health
        self.defense = 0

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.health_init()

    def health_init(self):
        left, top, width, height = self.bounding_rect
        self.health_bar = pygame.Rect((left, top + height, width, 8))

    def collision(self, x, y):
        return self.bounding_rect.collidepoint(x, y)

    def rescale(self, w, h):
        self.image = pygame.transform.scale(self.image, (w, h))

    def rescale_factor(self, n):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width // n, height // n))

    def reposition(self, x=None, y=None):
        if x:
            self.pos[X] = x
        if y:
            self.pos[Y] = y

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def get_img(self):
        return self.image

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.bounding_rect, 1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health(screen)

    def draw_health(self, screen):
        if self.defense:
            pygame.draw.rect(screen, BLUE, self.health_bar)
        else:
            pygame.draw.rect(screen, GRAY, self.health_bar)
            health = self.health_bar.copy()
            health.width *= self.current_health / self.max_health

class Player(Character):
    def __init__(self, image, health, x=0, y=0):
        super().__init__(image, health, x, y)
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
                self.deck = self.graveyard
                self.graveyard = []
            c = self.deck.pop()
            self.hand.add(c)

    def reset_decks(self):
        self.hand.empty()
        self.deck = self.all_cards.copy()
        random.shuffle(self.deck)
        self.graveyard = []
        self.in_play = []

class Enemy(Character):
    def __init__(self, image, health, x, y):
        super().__init__(image, health, x, y)
        self.defense = 0
        self.attacks = []
        self.attack_idx = 0

class Target(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Misc/red_target.png"), (24, 24))
        self.attack_img = pygame.transform.scale(pygame.image.load("assets/Misc/green_target.png"), (24, 24))
        self.boost_img = pygame.transform.scale(pygame.image.load("assets/Misc/blue_target.png"), (24, 24))
        self.rect = self.image.get_rect()

    def update(self, x, y):
        self.rect = self.image.get_rect(topleft=(x, y))

    def get_img(self):
        return self.image

    def get_atk(self):
        return self.attack_img

    def get_bst(self):
        return self.boost_img

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)
