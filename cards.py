import pygame
import os
from pygame.locals import *

BASE = os.path.join(os.getcwd(), "assets", "Cards")
WHITE = (255, 255, 255)
CYAN = (100, 150, 245)

CARD__WIDTH = 93
CARD_HEIGHT = 130
RES_WIDTH = 1400
RES_HEIGHT = 1000

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
        pth = os.path.join(BASE, image_path)
        self.image = pygame.transform.scale(pygame.image.load(pth), (CARD__WIDTH, CARD_HEIGHT))
        self.pos = [x, y]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.type = 'Attack'
        self.highlight = False

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)

    def show_box(self, screen, color, width=1):
        pygame.draw.rect(screen, color, self.rect, width)
