import pygame
import os
from pygame.locals import *
from battle import *

def main_map(screen):
    map_image = pygame.transform.scale(pygame.image.load('assets/map_icons/map.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.blit(map_image, (0, 0))

        #print(mouse)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            pygame.display.update()