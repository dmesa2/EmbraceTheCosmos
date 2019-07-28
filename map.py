import pygame
import os
from pygame.locals import *
from battle import *

class MapIcons(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        position = pygame.mouse.get_pos()
        for icon in self.sprites():
            icon.draw(screen, icon.collide(position))

class Icon(pygame.sprite.Sprite):
    def __init__(self, image, large_image, type, x, y):
        super().__init__()
        self.position = [x, y]
        self.type = type
        self.image = image
        self.large_image = large_image
        self.rect = self.image.get_rect(topleft=self.position)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center

    def draw(self, screen, large=False):
        if large:
            screen.blit(self.large_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def collide(self, position):
        return self.bounding_rect.collidepoint(position)

    def copy(self):
        return Icon(self.image, self.large_image, self.type, self.position[0], self.position[1])

class Map:
  def __init__(self):
     self.icons = MapIcons()
     #Boss
     bi = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech-small.png'), (70, 70))
     bi_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech.png'), (85, 85))
     self.icons.add(Icon(bi, bi_lg, 'boss', 355, 35))
     #Minions
     minion = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
     minion_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))
     self.icons.add(Icon(minion, minion_lg, 'minion', 65, 155))
     self.icons.add(Icon(minion, minion_lg, 'minion', 145, 190))
     #self.icons.add(Icon(minion, minion_lg, 'minion', 140, 90))
     self.icons.add(Icon(minion, minion_lg, 'minion', 122, 410))
     self.icons.add(Icon(minion, minion_lg, 'minion', 122, 498))
     self.icons.add(Icon(minion, minion_lg, 'minion', 192, 560))
     self.icons.add(Icon(minion, minion_lg, 'minion', 543, 186))
     self.icons.add(Icon(minion, minion_lg, 'minion', 610, 170))
     self.icons.add(Icon(minion, minion_lg, 'minion', 485, 420))
     self.icons.add(Icon(minion, minion_lg, 'minion', 670, 421))
     self.icons.add(Icon(minion, minion_lg, 'minion', 673, 505))
     self.icons.add(Icon(minion, minion_lg, 'minion', 750, 562))
     self.icons.add(Icon(minion, minion_lg, 'minion', 540, 560))

     #Stores
     store = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40))
     store_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50))
     self.icons.add(Icon(store, store_lg, 'shop', 121, 312))
     self.icons.add(Icon(store, store_lg, 'shop', 695, 151))
     self.icons.add(Icon(store, store_lg, 'shop', 602, 558))
     self.icons.add(Icon(store, store_lg, 'shop', 481, 500))

     #Unknown
     unk = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png'), (40, 40))
     unk_lg = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty.png'), (50, 50))
     self.icons.add(Icon(unk, unk_lg, 'unknown', 38, 550))
     self.icons.add(Icon(unk, unk_lg, 'unknown', 408, 560))
     self.icons.add(Icon(unk, unk_lg, 'unknown', 570, 320))

     self.bg = pygame.transform.scale(pygame.image.load('assets/map_icons/map.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

     #Legend
     self.legend = pygame.transform.scale(pygame.image.load('assets/map_icons/Legend.png'), (200, 50))

  def main_map(self, screen, player, assets):
      while True:
        screen.blit(self.bg, (0, 0))
        screen.blit(self.legend, (580, 20))
        self.icons.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            elif event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                for sp in self.icons.sprites():
                    if sp.collide(position) and sp.type == 'minion':
                        battle(screen, player, assets)

            pygame.display.update()
