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

   left_side_minion_one(screen)
   left_side_minion_two(screen)
   left_side_minion_three(screen)
   left_side_minion_four(screen)
   left_side_minion_five(screen)

   right_side_minion_one(screen)
   right_side_minion_two(screen)
   right_side_minion_three(screen)
   right_side_minion_four(screen)
   right_side_minion_five(screen)
   right_side_minion_six(screen)
   right_side_minion_seven(screen)

   left_side_store(screen)

   right_side_store_one(screen)
   right_side_store_two(screen)
   right_side_store_three(screen)

   unknown_left(screen)

   unknown_right_one(screen)
   unknown_right_two(screen)

def boss_icon(screen):
   boss = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech-small.png'), (70, 70))
   boss_large = pygame.transform.scale(pygame.image.load('assets/map_icons/battle-mech.png'), (85, 85)) 

   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()

   if 355+170 > mouse[0] > 355 and 50+35 > mouse[1] > 50:
       screen.blit(boss_large, (348,35))
   else:
      screen.blit(boss, (355,35))

def left_side_minion_one(screen):
    minion1 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion1_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 65+30 > mouse[0] > 65 and 50+155 > mouse[1] > 50:
       screen.blit(minion1_large, (60,155))
    else:
     screen.blit(minion1, (65,155))

def left_side_minion_two(screen):
    minion2 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion2_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 145+30 > mouse[0] > 145 and 50+190 > mouse[1] > 50:
       screen.blit(minion2_large, (140,190))
    else:
     screen.blit(minion2, (145,190))

def left_side_minion_three(screen):
    minion3 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion3_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 122+30 > mouse[0] > 122 and 50+410 > mouse[1] > 50:
       screen.blit(minion3_large, (117,410))
    else:
     screen.blit(minion3, (122,410))
 
def left_side_minion_four(screen):
    minion4 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion4_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 122+30 > mouse[0] > 122 and 50+498 > mouse[1] > 50:
       screen.blit(minion4_large, (117,498))
    else:
     screen.blit(minion4, (122,498))

def left_side_minion_five(screen):
    minion5 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion5_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 192+30 > mouse[0] > 192 and 50+560 > mouse[1] > 50:
       screen.blit(minion5_large, (187,560))
    else:
     screen.blit(minion5, (192,560))

def right_side_minion_one(screen):
    minion6 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion6_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 543+30 > mouse[0] > 543 and 50+186 > mouse[1] > 50:
       screen.blit(minion6_large, (538,186))
    else:
     screen.blit(minion6, (543,186))

def right_side_minion_two(screen):
    minion7 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion7_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 610+30 > mouse[0] > 610 and 50+170 > mouse[1] > 50:
       screen.blit(minion7_large, (605,170))
    else:
     screen.blit(minion7, (610,170))

def right_side_minion_three(screen):
    minion8 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion8_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 485+30 > mouse[0] > 485 and 50+420 > mouse[1] > 50:
       screen.blit(minion8_large, (480,420))
    else:
     screen.blit(minion8, (485,420))

def right_side_minion_four(screen):
    minion9 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion9_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 670+30 > mouse[0] > 670 and 50+421 > mouse[1] > 50:
       screen.blit(minion9_large, (665,421))
    else:
     screen.blit(minion9, (670,421))

def right_side_minion_five(screen):
    minion10 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion10_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 673+30 > mouse[0] > 673 and 50+505 > mouse[1] > 50:
       screen.blit(minion10_large, (668,505))
    else:
     screen.blit(minion10, (673,505))

def right_side_minion_six(screen):
    minion11 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion11_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 750+30 > mouse[0] > 750 and 50+562 > mouse[1] > 50:
       screen.blit(minion11_large, (745,562))
    else:
     screen.blit(minion11, (750,562))

def right_side_minion_seven(screen):
    minion12 = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot-small.png'), (40, 40))
    minion12_large = pygame.transform.scale(pygame.image.load('assets/map_icons/spider-bot.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 540+30 > mouse[0] > 540 and 50+562 > mouse[1] > 50:
       screen.blit(minion12_large, (535,562))
    else:
     screen.blit(minion12, (540,562))

def left_side_store(screen):
    store1 = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40))
    store1_large = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 121+30 > mouse[0] > 121 and 50+312 > mouse[1] > 50:
       screen.blit(store1_large, (116,312))
    else:
     screen.blit(store1, (121,312))

def right_side_store_one(screen):
    store2 = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40))
    store2_large = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 695+30 > mouse[0] > 695 and 50+151 > mouse[1] > 50:
       screen.blit(store2_large, (690,151))
    else:
     screen.blit(store2, (695,151))

def right_side_store_two(screen):
    store3 = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40))
    store3_large = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 602+30 > mouse[0] > 602 and 50+561 > mouse[1] > 50:
       screen.blit(store3_large, (597,553))
    else:
      screen.blit(store3, (602,558))

def right_side_store_three(screen):
    store4 = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank-small.png'), (40, 40))
    store4_large = pygame.transform.scale(pygame.image.load('assets/map_icons/energy-tank.png'), (50, 50)) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 481+30 > mouse[0] > 481 and 50+500 > mouse[1] > 50:
       screen.blit(store4_large, (476,500))
    else:
      screen.blit(store4, (481,500))

def unknown_left(screen):
   unnkown1 = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png'), (40, 40))
   unknown1_large = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty.png'), (50, 50)) 

   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()

   if 38+30 > mouse[0] > 38 and 50+560 > mouse[1] > 50:
     screen.blit(unknown1_large, (33,560))
   else:
     screen.blit(unnkown1, (38,560))

def unknown_right_one(screen):
   unnkown2 = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png'), (40, 40))
   unknown2_large = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty.png'), (50, 50)) 

   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()

   if 408+30 > mouse[0] > 408 and 50+560 > mouse[1] > 50:
     screen.blit(unknown2_large, (403,560))
   else:
     screen.blit(unnkown2, (408,560))

def unknown_right_two(screen):
   unnkown3 = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty-small.png'), (40, 40))
   unknown3_large = pygame.transform.scale(pygame.image.load('assets/map_icons/uncertainty.png'), (50, 50)) 

   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()

   if 570+30 > mouse[0] > 570 and 50+320 > mouse[1] > 50:
     screen.blit(unknown3_large, (565,320))
   else:
     screen.blit(unnkown3, (570,320))