import pygame
import os
from pygame.locals import *
from battle import *

def main_map(screen):
    map_image = pygame.transform.scale(pygame.image.load('assets/map_icons/map.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.blit(map_image, (0, 0))
        main_icons(screen)
       # print(mouse)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            pygame.display.update()

def main_icons(screen):
   boss_icon(screen)
   left_side_minions(screen)

def boss_icon(screen):
   boss = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech-small.png'), (50, 50))
   boss_large = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech.png'), (60, 60)) 

   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()

   if 370+170 > mouse[0] > 370 and 50+50 > mouse[1] > 50:
       screen.blit(boss_large, (365,50))
   else:
      screen.blit(boss, (370,50))

def left_side_minions(screen):
    minion1 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion1_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 65+30 > mouse[0] > 65 and 50+155 > mouse[1] > 50:
       screen.blit(minion1_large, (60,155))
    else:
     screen.blit(minion1, (65,155))
