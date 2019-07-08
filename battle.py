import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys
from cards import Card, Hand
from character import *

ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
SHIPS_PATH = os.path.join("Spaceships", "spaceships", "parts_spriter_animation")
CARD_PATH = os.path.join(ASSETS_PATH, "Cards")
# declare the size of the map
WIDTH = 1400
HEIGHT = 1000
CARD__WIDTH = 93
CARD_HEIGHT = 130

white = (200, 200, 200) 
green = (0, 200, 0) 
blue = (0, 0, 200)
black = (0,0,0)
gray = (128,128,128)

bright_white = (255,255,255)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_gray = (169,169,169)

def main_menu(screen, myfont):
    text = myfont.render("Play", True, black) 
    text2 = myfont.render("Help", True, black)
    text3 = myfont.render("Quit", True, black)
    menu_image = pygame.image.load('assets/Background/Embrace_The_Cosmos.png')
    pygame.mixer.music.load('assets/Sound/Sounds_1/Parabola.mp3')
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(menu, (0, 0))
        screen.blit(menu_image,(325,50))

        buttons(screen,text,text2,text3)

        #print(mouse)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
            pygame.display.update()

# For the button function, I used sentdex tutorials from youtube.com 
# as a reference
def buttons(screen,text,text2,text3):
    pygame.draw.rect(screen, gray,(640,350,170,50))
    pygame.draw.rect(screen, gray,(640,450,170,50))
    pygame.draw.rect(screen, gray,(640,550,170,50))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 640+170 > mouse[0] > 640 and 350+50 > mouse[1] > 350:
        pygame.draw.rect(screen, bright_gray,(640,350,170,50))
        if click[0] == 1:
           battle(screen, pg) 
    else:
        pygame.draw.rect(screen, gray,(640,350,170,50))
        
    if 640+170 > mouse[0] > 640 and 450+50 > mouse[1] > 450:
         pygame.draw.rect(screen, bright_gray,(640,450,170,50))
    else:
        pygame.draw.rect(screen, gray,(640,450,170,50))

    if 640+170 > mouse[0] > 640 and 550+50 > mouse[1] > 550:
        pygame.draw.rect(screen, bright_gray,(640,550,170,50))
        if click[0] == 1:
            #pygame.quit()
            sys.exit()
    else:
        pygame.draw.rect(screen, gray,(640,550,170,50))

    screen.blit(text,(690,360))
    screen.blit(text2,(690,460))
    screen.blit(text3, (690,560))

def targeting(screen, bg, pg, eg, hand):
    pygame.mouse.set_visible(False)
    target = Target()
    targeted = False
    while pygame.mouse.get_pressed()[0]:
        screen.blit(bg, (0, 0))
        hand.draw_hand(screen)
        pg.draw(screen)
        eg.draw(screen)
        eg.draw_rect(screen)
        pg.draw_rect(screen)
        mX, mY = pygame.mouse.get_pos()
        target.update(mX, mY)
        #if any(pygame.sprite.spritecollide(target, eg, False)):
        if any([sp.collision(mX, mY) for sp in eg]):
            screen.blit(target.get_atk(), (mX, mY))
        elif any([sp.collision(mX, mY) for sp in pg]):
            screen.blit(target.get_bst(), (mX, mY))
        else:
            screen.blit(target.get_img(), (mX, mY))
        pygame.event.pump()
        pygame.display.update()
    pygame.mouse.set_visible(True)
    return

def battle(screen, pg):
    eg = Enemy()
    enemy0 = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship4/Ship4.png'), 900, 300)
    enemy1 = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship2/Ship2.png'), 800, 450)
    enemy2 = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship5/Ship5.png'), 900, 650)
    eg.add(enemy0, enemy1, enemy2)
    for e in eg:
        e.flip()
    eg.update()
    pg.update()
    hand = Hand()
    hand.add(Card("C_Laser_Cannon.png", WIDTH / 2 - CARD__WIDTH / 2, HEIGHT - CARD_HEIGHT),
             Card("C_Shield.png", WIDTH / 2 + CARD__WIDTH / 2, HEIGHT - CARD_HEIGHT))
    hand.update()
    pygame.mouse.set_visible(True)

    while True:
        screen.blit(bg, (0, 0))
        hand.ddraw(screen, pygame.mouse.get_pos())
        # place the player object (the loaded image)
        for p in pg:
            screen.blit(p.get_img(), player.pos)
        for e in eg:
            screen.blit(e.get_img(), e.pos)
            screen.blit(e.get_img(), e.pos)
            screen.blit(e.get_img(), e.pos)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                for card in hand:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card.highlight = True
                        targeting(screen, bg, pg, eg, hand)
                        card.highlight = False
                        break

            # update the display every iteration of this loop
            pygame.display.update()

if __name__=='__main__':
    pygame.init()
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init()
    
    myfont = pygame.font.Font('freesansbold.ttf', 32)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # initilaize the game object

    # intialize the display surface. this surface is what pygame draws
    # things on
    bg = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, "Background", "spacefield_a-000.png")), (WIDTH, HEIGHT))
    menu = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, "Background", "nebula01.png")), (WIDTH, HEIGHT))
    pg = Player()
    player = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship3/Ship3.png'), 100, 500)
    pg.add(player)

    main_menu(screen,myfont)
    #battle(screen, pg)