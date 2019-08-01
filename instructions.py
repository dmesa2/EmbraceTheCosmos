import os
import pygame
from pygame.locals import *
import sys
from gamestate import *


class Instructions:
  def __init__(self):
     self.bg = pygame.transform.scale(pygame.image.load('assets/Instructions/Instructions.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))


  def buttons(self,screen):
    myfont = pygame.font.Font('freesansbold.ttf', 32)
    text3 = myfont.render("Back", True, BLACK)
    while True:
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if 310+170 > mouse[0] > 310 and 530+50 > mouse[1] > 530:
          pygame.draw.rect(screen, GRAY,(310,530,170,50))
          pygame.draw.rect(screen, BRIGHT_GRAY,(310,530,170,50))
          if click[0] == 1:
              #pygame.quit()
              #sys.exit()
              return False
      else:
          pygame.draw.rect(screen, GRAY,(310,530,170,50))

      screen.blit(text3, (355,540))
      pygame.display.update()
      pygame.event.pump()
    return True

  def instructions_menu(self, screen):
      ret = True
      while ret:
        screen.blit(self.bg, (0, 0))
        ret = self.buttons(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            pygame.display.update()