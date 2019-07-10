import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys
from cards import Card, Hand
from character import Player, Enemy, Character, Target
from gamestate import *

def targeting(screen, bg, player_group, enemy_group, hand):
    '''
    Function called when a card is selected by the player
    Sucessful targeting means the card is used
    Otherwise the game state returns to as it was
    '''
    pygame.mouse.set_visible(False)
    target = Target()
    targeted = False
    while pygame.mouse.get_pressed()[0]:
        pygame.time.Clock().tick(40)
        screen.blit(bg, (0, 0))
        hand.draw_hand(screen)
        player_group.draw(screen)
        enemy_group.draw(screen)
        enemy_group.draw_rect(screen)
        player_group.draw_rect(screen)
        mX, mY = pygame.mouse.get_pos()
        target.update(mX, mY)
        # If a sucessful collisoin with the enemy is detected
        if any([sp.collision(mX, mY) for sp in enemy_group]):
            screen.blit(target.get_atk(), (mX, mY))
        # If a sucessful collision with the player is detected
        elif any([sp.collision(mX, mY) for sp in player_group]):
            screen.blit(target.get_bst(), (mX, mY))
        else:
            screen.blit(target.get_img(), (mX, mY))
        pygame.event.pump()
        pygame.display.update()
    pygame.mouse.set_visible(True)
    return

def battle(screen, player_group):
    background = pygame.transform.scale(pygame.image.load(
            os.path.join(ASSETS_PATH, "Background", "spacefield_a-000.png")),
            (SCREEN_WIDTH, SCREEN_HEIGHT))
    enemy_group = Enemy()
    # change to dynamically create enemies
    enemy0 = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship4/Ship4.png'),
        SCREEN_WIDTH - 100, SCREEN_HEIGHT / 2 + 50)
    enemy1 = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship2/Ship2.png'),
        SCREEN_WIDTH - 200, SCREEN_HEIGHT / 2 - 50)
    enemy2 = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship5/Ship5.png'),
        SCREEN_WIDTH - 100, SCREEN_HEIGHT / 2)
    enemy_group.add(enemy0, enemy1, enemy2)
    for enemy in enemy_group:
        enemy.flip()
    enemy_group.update()

    player_group.update()
    hand = Hand()
    # change to draw function
    hand.add(Card("C_Laser_Cannon.png", SCREEN_WIDTH / 2 - CARD__WIDTH / 2, SCREEN_HEIGHT - CARD_HEIGHT),
             Card("C_Shield.png", SCREEN_WIDTH / 2 + CARD__WIDTH / 2, SCREEN_HEIGHT - CARD_HEIGHT))
    hand.update()
    pygame.mouse.set_visible(True)
    while True:
        pygame.time.Clock().tick(40)
        # draw background
        screen.blit(background, (0, 0))
        # dynamic hand animation
        hand.ddraw(screen, pygame.mouse.get_pos())
        # place the player object (the loaded image)
        player_group.draw(screen)
        for player in player_group:
            screen.blit(player.image, player.rect)
        enemy_group.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                for card in hand:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card.highlight = True
                        targeting(screen, background, player_group, enemy_group, hand)
                        card.highlight = False
                        break

            # update the display every iteration of this loop
            pygame.display.update()

if __name__ == "__main__":
    # Run battle.py directly to test battle functionality
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # declare the size of the map

    player_group = Player()
    player = Character(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship3/Ship3.png'),
            0, 300)

    player_group.add(player)

    battle(screen, player_group)
