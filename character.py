import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import sprite

WHITE = (255, 255, 255)
X = 0
Y = 1

class Player(sprite.Group):
    def __init__(self):
        super().__init__()

    def draw_rect(self, screen):
        for s in self.sprites():
            s.show_box(screen)

class Enemy(sprite.Group):
    def __init__(self):
        super().__init__()

    def draw_rect(self, screen):
        for s in self.sprites():
            s.show_box(screen)

class Character(sprite.Sprite):
    def __init__(self, image, x=0, y=0):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load(image))
        self.pos = [x, y]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect2 = self.image.get_bounding_rect()
        self.rect2.center = self.rect.center
        
    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)

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
        pygame.draw.rect(screen, WHITE, self.rect2, 1)

class Target(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Misc/red_target.png"), (24, 24))
        self.alternate = pygame.transform.scale(pygame.image.load("assets/Misc/green_target.png"), (24, 24))
        self.rect = self.image.get_rect()

    def update(self, x, y):
        self.rect = self.image.get_rect(topleft=(x, y))

    def get_img(self):
        return self.image

    def alt_img(self):
        return self.alternate

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)
