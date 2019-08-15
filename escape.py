import os
import pygame
from pygame.locals import *
import sys
from gamestate import *

class Escape:
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load('assets/Instructions/Instructions_Background.png'), (200, 200))


    def buttons(self,screen):
        myfont = pygame.font.Font('freesansbold.ttf', 32)
        text2 = myfont.render("Back", True, BLACK) 
        text3 = myfont.render("Quit", True, BLACK)

        while True:
          pygame.time.Clock().tick(40)
          mouse = pygame.mouse.get_pos()
          click = pygame.mouse.get_pressed()

          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                return False             

          if 340+170 > mouse[0] > 340 and 240+50 > mouse[1] > 240:
            pygame.draw.rect(screen, BRIGHT_GRAY,(340,240,170,50))
            if click[0] == 1:
                return False      
          
          elif 340+170 > mouse[0] > 340 and 320+50 > mouse[1] > 320:
            pygame.draw.rect(screen, BRIGHT_GRAY,(340,320,170,50))
            if click[0] == 1:
                sys.exit()
                
          else:
            pygame.draw.rect(screen, GRAY,(340,240,170,50))
            pygame.draw.rect(screen, GRAY,(340,320,170,50))

          screen.blit(text2, (385, 250))
          screen.blit(text3, (385,330))
          pygame.display.update()
          pygame.event.pump()
        return True

    def escape_menu(self, screen):
      ret = True
      while ret:
        pygame.time.Clock().tick(40)
        screen.blit(self.bg, (325, 200))
        for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
              break
        pygame.display.update()
        ret = self.buttons(screen)
