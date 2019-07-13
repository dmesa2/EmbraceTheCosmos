import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys
import cards
from character import Player, Enemy, Enemy_Gr, Character, Target
from gamestate import *

def targeting(screen, bg, card, player, enemy_group):
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
        player.hand.draw(screen)
        player.draw(screen)
        enemy_group.draw(screen)
        enemy_group.draw_rect(screen)
        player.show_box(screen)
        mX, mY = pygame.mouse.get_pos()
        target.update(mX, mY)
        if card.ctype == 'TARGET_ATTACK':
            # If a sucessful collisoin with the enemy is detected
            if any([sp.collision(mX, mY) for sp in enemy_group]):
                screen.blit(target.get_atk(), (mX, mY))
            else:
                screen.blit(target.get_img(), (mX, mY))
        else:
            screen.blit(target.get_img(), (mX, mY))
        pygame.event.pump()
        pygame.display.update()
    pygame.mouse.set_visible(True)
    return

def battle(screen, player):
    background = pygame.transform.scale(pygame.image.load(
            os.path.join(ASSETS_PATH, "Background", "spacefield_a-000.png")),
            (SCREEN_WIDTH, SCREEN_HEIGHT))
    enemy_group = Enemy_Gr()
    # change to dynamically create enemies
    enemy0 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship4/Ship4.png'), 30,
        SCREEN_WIDTH - 200, SCREEN_HEIGHT / 2 -100)
    enemy1 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship2/Ship2.png'), 20,
        SCREEN_WIDTH - 150, SCREEN_HEIGHT / 2 - 200)
    enemy2 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship5/Ship5.png'), 30,
        SCREEN_WIDTH - 150, SCREEN_HEIGHT / 2)
    enemy_group.add(enemy0, enemy1, enemy2)
    for enemy in enemy_group:
        enemy.flip()
    enemy_group.update()

    player.update()
    player.reset_decks()
    player.draw_hand()
    player.hand.draw(screen)
    player.hand.position_hand()
    # change to draw function
    pygame.mouse.set_visible(True)
    while True:
        pygame.time.Clock().tick(40)
        # draw background
        screen.blit(background, (0, 0))
        # dynamic hand animation
        player.hand.ddraw(screen, pygame.mouse.get_pos())
        # place the player object (the loaded image)
        player.draw(screen)
        enemy_group.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                for card in player.hand:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card.highlight = True
                        targeting(screen, background, card, player, enemy_group)
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

    player = Player(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship3/Ship3.png'),
            40, 0, SCREEN_HEIGHT / 3)
    all_cards = cards.load_cards(os.path.join(ASSETS_PATH, CARD_PATH, 'cards.json'))
    for _ in range(3):
        player.all_cards.append(all_cards[0].copy())
        player.all_cards.append(all_cards[1].copy())
        player.all_cards.append(all_cards[2].copy())
    battle(screen, player)
