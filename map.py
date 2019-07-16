import pygame
import os
from pygame.locals import *
from battle import *

class Map:
  def __init__(self):

     #declaring array
     self.array = []

     #boss
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech-small.png'), (70, 70)))#[0]
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech.png'), (85, 85))) #[1]

     #minions
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40)))#[2]
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)))#[3]

     #stores
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40)))#[4]
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50)))#[5]

     #unknown
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png'), (40, 40)))#[6]
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty.png'), (50, 50)))#[7]

     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/map.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)))#[8]

     #legend
     self.array.append(pygame.transform.scale(pygame.image.load('assets/map_icons/Legend.png'), (200, 50)))#[9]

  def boss_icon(self,screen):
    boss = self.array[0]
    boss_large = self.array[1] 
    
    rect = boss.get_rect(topleft=(355,35))
    rect2 = boss.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(boss_large, (348,35))
    else:
       screen.blit(boss, (355,35))

  def left_side_minion_one(self,screen):
    minion1 = self.array[2]
    minion1_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion1.get_rect(topleft=(65,155))
    rect2 = minion1.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion1_large, (60,155))
    else:
       screen.blit(minion1, (65,155))

  def left_side_minion_two(self,screen):
    minion2 = self.array[2]
    minion2_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion2.get_rect(topleft=(145,190))
    rect2 = minion2.get_bounding_rect()
    rect2.center = rect.center
    
    #pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion2_large, (140,190))
    else:
       screen.blit(minion2, (145,190))

  def left_side_minion_three(self,screen):
    minion3 = self.array[2]
    minion3_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion3.get_rect(topleft=(122,410))
    rect2 = minion3.get_bounding_rect()
    rect2.center = rect.center
    
    #pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion3_large, (122,410))
    else:
       screen.blit(minion3, (117,410))

  def left_side_minion_four(self,screen):
    minion4 = self.array[2]
    minion4_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion4.get_rect(topleft=(122,498))
    rect2 = minion4.get_bounding_rect()
    rect2.center = rect.center
    
    #pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion4_large, (117,498))
    else:
       screen.blit(minion4, (122,498))

  def left_side_minion_five(self,screen):
    minion5 = self.array[2]
    minion5_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion5.get_rect(topleft=(192,560))
    rect2 = minion5.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion5_large, (187,560))
    else:
       screen.blit(minion5, (192,560))

  def right_side_minion_one(self,screen):

    minion6 = self.array[2]
    minion6_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion6.get_rect(topleft=(543,186))
    rect2 = minion6.get_bounding_rect()
    rect2.center = rect.center
    
  #  pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion6_large, (538,186))
    else:
       screen.blit(minion6, (543,186))

  def right_side_minion_two(self,screen):

    minion7 = self.array[2]
    minion7_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion7.get_rect(topleft=(610,170))
    rect2 = minion7.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion7_large, (615,170))
    else:
       screen.blit(minion7, (610,170))

  def right_side_minion_three(self,screen):

    minion8 = self.array[2]
    minion8_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion8.get_rect(topleft=(485,420))
    rect2 = minion8.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion8_large, (480,420))
    else:
       screen.blit(minion8, (485,420))

  def right_side_minion_four(self,screen):

    minion9 = self.array[2]
    minion9_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion9.get_rect(topleft=(670,421))
    rect2 = minion9.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion9_large, (665,421))
    else:
       screen.blit(minion9, (670,421))

  def right_side_minion_five(self,screen):

    minion10 = self.array[2]
    minion10_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion10.get_rect(topleft=(673,505))
    rect2 = minion10.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion10_large, (668,505))
    else:
       screen.blit(minion10, (673,505))

  def right_side_minion_six(self,screen):

    minion11 = self.array[2]
    minion11_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion11.get_rect(topleft=(750,562))
    rect2 = minion11.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion11_large, (745,562))
    else:
       screen.blit(minion11, (750,562))

  def right_side_minion_seven(self,screen):

    minion12 = self.array[2]
    minion12_large = self.array[3]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = minion12.get_rect(topleft=(540,560))
    rect2 = minion12.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(minion12_large, (535,560))
    else:
       screen.blit(minion12, (540,560))

  def left_side_store(self,screen):

    store1 = self.array[4]
    store1_large = self.array[5]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = store1.get_rect(topleft=(121,312))
    rect2 = store1.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(store1_large, (116,312))
    else:
       screen.blit(store1, (121,312))


  def right_side_store_one(self,screen):
    store2 = self.array[4]
    store2_large = self.array[5]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = store2.get_rect(topleft=(695,151))
    rect2 = store2.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(store2_large, (690,151))
    else:
       screen.blit(store2, (695,151))

  def right_side_store_two(self,screen):
    store3 = self.array[4]
    store3_large = self.array[5]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = store3.get_rect(topleft=(602,558))
    rect2 = store3.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(store3_large, (597,558))
    else:
       screen.blit(store3, (602,558))

  def right_side_store_three(self,screen):
    store4 = self.array[4]
    store4_large = self.array[5]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = store4.get_rect(topleft=(481,500))
    rect2 = store4.get_bounding_rect()
    rect2.center = rect.center
    
  #  pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(store4_large, (476,500))
    else:
       screen.blit(store4, (481,500))

  def unknown_left(self,screen):
    unknown1 = self.array[6]
    unknown1_large = self.array[7]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = unknown1.get_rect(topleft=(38,550))
    rect2 = unknown1.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(unknown1_large, (33,550))
    else:
       screen.blit(unknown1, (38,550))

  def unknown_right_one(self,screen):
    unknown2 = self.array[6]
    unknown2_large = self.array[7]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = unknown2.get_rect(topleft=(408,560))
    rect2 = unknown2.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(unknown2_large, (403,560))
    else:
       screen.blit(unknown2, (408,560))

  def unknown_right_two(self,screen):
    unknown3 = self.array[6]
    unknown3_large = self.array[7]

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = unknown3.get_rect(topleft=(570,320))
    rect2 = unknown3.get_bounding_rect()
    rect2.center = rect.center
    
   # pygame.draw.rect(screen,WHITE, rect2,1)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect2.collidepoint(mouse): 
      screen.blit(unknown3_large, (565,320))
    else:
       screen.blit(unknown3, (570,320))


  def main_icons(self,screen):
      self.boss_icon(screen)

      self.left_side_minion_one(screen)
      self.left_side_minion_two(screen)
      self.left_side_minion_three(screen)
      self.left_side_minion_four(screen)
      self.left_side_minion_five(screen)

      self.right_side_minion_one(screen)
      self.right_side_minion_two(screen)
      self.right_side_minion_three(screen)
      self.right_side_minion_four(screen)
      self.right_side_minion_five(screen)
      self.right_side_minion_six(screen)
      self.right_side_minion_seven(screen)

      self.left_side_store(screen)

      self.right_side_store_one(screen)
      self.right_side_store_two(screen)
      self.right_side_store_three(screen)

      self.unknown_left(screen)

      self.unknown_right_one(screen)
      self.unknown_right_two(screen)

  def main_map(self,screen):
      map_image = self.array[8]
      legend = self.array[9]
      while True:
        screen.blit(map_image, (0, 0))
        screen.blit(legend, (580,20))
        self.main_icons(screen)
       # print(mouse)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            pygame.display.update()