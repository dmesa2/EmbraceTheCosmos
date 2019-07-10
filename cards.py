import pygame
import os
from pygame.locals import *
from gamestate import *
BASE = os.path.join(os.getcwd(), "assets", "Cards")

class Hand(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw_rect(self, screen):
        for s in self.sprites():
            s.show_box(screen, WHITE)

    def draw_hand(self, screen):
        for card in self.sprites():
            screen.blit(card.image, card.rect)
            if card.highlight:
                card.show_box(screen, CYAN, 2)
    def ddraw(self, screen, position):
        for card in self.sprites():
            screen.blit(card.image, card.rect)
            if card.rect.collidepoint(position):
                card.show_box(screen, CYAN, 2)

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path, x=0, y=0):
        super().__init__()
        pth = os.path.join(CARD_PATH, image_path)
        self.id = None
        self.image = pygame.transform.scale(pygame.image.load(pth), (CARD_WIDTH, CARD_HEIGHT))
        self.pos = [x, y]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.highlight = False
        # EFFECTS
        # TARGET_ATTACK, AREA_ATTACK, BOOST, POWER
        self.type = None
        # Power cost to ship
        self.cost = 0
        # Dictionary to hold alternate effects
        self.status_effect = dict()
        # Player Class e.g. FIGHTER or NEUTRAL
        self.class = None
        self.damage = None
        self.defense = None

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)

    def show_box(self, screen, color, width=1):
        pygame.draw.rect(screen, color, self.rect, width)
