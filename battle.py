import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys
import cards
from character import Player, Enemy, Enemy_Gr, Character, Target
from gamestate import *
from buttons import Button, GameBoard


def targeting(screen, board, card, player, enemy_group):
    '''
    Function called when a card is selected by the player
    Sucessful targeting means the card is used
    Otherwise the game state returns to as it was
    '''
    pygame.mouse.set_visible(False)
    target = Target()
    targeted = False
    ret = False
    card_area = player.hand.get_area()
    while pygame.mouse.get_pressed()[0]:
        pygame.time.Clock().tick(40)
        board.draw(screen)
        #board._show_boxes(screen)
        player.hand.draw(screen)
        player.draw(screen)
        enemy_group.draw(screen)
        #enemy_group.draw_rect(screen)
        #player.show_box(screen)
        mX, mY = pygame.mouse.get_pos()
        target.update(mX, mY)
        pygame.draw.rect(screen, WHITE, card_area, 1)
        if card.ctype == 'TARGET_ATTACK':
            # changes targeting recticle if a sucessful
            # collisoin with the enemy is detected
            if any([sp.collision(mX, mY) for sp in enemy_group]):
                screen.blit(target.get_atk(), (mX, mY))
            else:
                screen.blit(target.get_img(), (mX, mY))
        else:
            # non targeted attack
            # highlights targeting recticle if outside card area
            if not card_area.collidepoint(mX, mY):
                screen.blit(target.get_bst(), (mX, mY))
            else:
                screen.blit(target.get_img(), (mX, mY))

        pygame.event.pump()
        pygame.display.update()
    if card.ctype == 'TARGET_ATTACK':
        targeted = [sp for sp in enemy_group if sp.collision(mX, mY)]
        if targeted:
            player.hand.remove(card)
            player.graveyard.append(card)
            enemy_group.process_attack(card, targeted[0])
            ret = True
    else:
        if not card_area.collidepoint(mX, mY):
            if card.ctype == 'BOOST':
                player.shield += card.shield
                player.hand.remove(card)
                player.graveyard.append(card)
                ret = True
            elif card.ctype == 'AREA_ATTACK':
                player.hand.remove(card)
                player.graveyard.append(card)
                enemy_group.process_attack(card)
                ret = True
    pygame.mouse.set_visible(True)
    return ret

def battle(screen, player):
    board = GameBoard("spacefield_a-000.png")
    enemy_group = Enemy_Gr()
    # change to dynamically create enemies
    enemy0 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship4/Ship4.png'), 15,
        SCREEN_WIDTH - 200, SCREEN_HEIGHT / 2 -100)
    enemy1 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship2/Ship2.png'), 15,
        SCREEN_WIDTH - 150, SCREEN_HEIGHT / 2 - 200)
    enemy2 = Enemy(os.path.join(ASSETS_PATH, SHIPS_PATH, 'Ship5/Ship5.png'), 10,
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
        board.draw(screen)
        # dynamic hand animation
        player.hand.ddraw(screen, pygame.mouse.get_pos())
        # place the player object (the loaded image)
        player.draw(screen)
        enemy_group.draw(screen)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if board.end_turn.collision(mouse_pos):
                    player.end_turn(board)
                else:
                    for card in player.hand:
                        if card.rect.collidepoint(mouse_pos):
                            card.highlight = True
                            if targeting(screen, board, card, player, enemy_group):
                                player.hand.position_hand()
                            card.highlight = False
                            break

            elif event.type == MOUSEMOTION:
                board.highlight(screen, mouse_pos)

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
    for _ in range(4):
        player.all_cards.append(all_cards[0].copy())
        player.all_cards.append(all_cards[1].copy())
    player.all_cards.append(all_cards[2].copy())
    player.all_cards.append(all_cards[2].copy())
    battle(screen, player)
