import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys
from battle import *
from cards import Card, Hand
from character import *
from gamestate import *
from map import *

def main_menu(screen, myfont,pg,map_call):
    text = myfont.render("Play", True, BLACK) 
    text2 = myfont.render("Help", True, BLACK)
    text3 = myfont.render("Quit", True, BLACK)
    menu_image = pygame.image.load('assets/Background/Embrace_The_Cosmos.png')
    pygame.mixer.music.load('assets/Sound/Sounds_1/Parabola.mp3')
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(menu, (0, 0))
        screen.blit(menu_image,(5,50))

        buttons(screen,text,text2,text3,pg,map_call)

        #print(mouse)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            pygame.display.update()

# For the button function, I used sentdex tutorials from youtube.com 
# as a reference
def buttons(screen,text,text2,text3,pg,map_call):
    pygame.draw.rect(screen, GRAY,(340,250,170,50))
    pygame.draw.rect(screen, GRAY,(340,350,170,50))
    pygame.draw.rect(screen, GRAY,(340,450,170,50))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 340+170 > mouse[0] > 340 and 250+50 > mouse[1] > 250:
        pygame.draw.rect(screen, BRIGHT_GRAY,(340,250,170,50))
        if click[0] == 1:
           #battle(screen, pg)
           map_call.main_map(screen)
    else:
        pygame.draw.rect(screen, GRAY,(340,250,170,50))
        
    if 340+170 > mouse[0] > 340 and 350+50 > mouse[1] > 350:
         pygame.draw.rect(screen, BRIGHT_GRAY,(340,350,170,50))
    else:
        pygame.draw.rect(screen, GRAY,(340,350,170,50))

    if 340+170 > mouse[0] > 340 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(screen, BRIGHT_GRAY,(340,450,170,50))
        if click[0] == 1:
            #pygame.quit()
            sys.exit()
    else:
        pygame.draw.rect(screen, GRAY,(340,450,170,50))

    screen.blit(text,(390,260))
    screen.blit(text2,(390,360))
    screen.blit(text3, (390,460))

if __name__=='__main__':
    pygame.init()
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init()
    
    myfont = pygame.font.Font('freesansbold.ttf', 32)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # initilaize the game object

    # intialize the display surface. this surface is what pygame draws
    # things on
    bg = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, "Background", "spacefield_a-000.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, "Background", "nebula01.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pg = Player()
    player = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship3/Ship3.png'), 100, 500)
    pg.add(player)
    map_call = Map()


    main_menu(screen,myfont,pg,map_call)
    #battle(screen, pg)
