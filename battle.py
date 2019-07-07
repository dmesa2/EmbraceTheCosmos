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
            screen.blit(target.alt_img(), (mX, mY))
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
    hand.add(Card("C_Laser_Cannon.png", 600, HEIGHT - CARD_HEIGHT),
             Card("C_Shield.png", 693, HEIGHT - CARD_HEIGHT))
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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # initilaize the game object

    # intialize the display surface. this surface is what pygame draws
    # things on
    bg = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, "Background", "spacefield_a-000.png")), (WIDTH, HEIGHT))

    pg = Player()
    player = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship3/Ship3.png'), 100, 500)
    pg.add(player)
    battle(screen, pg)
