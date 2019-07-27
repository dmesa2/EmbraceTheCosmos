import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys
import cards
from character import Player, Enemy, EnemyFleet, Character, Target
from gamestate import *
from buttons import Button, GameBoard
from gameassets import GameAssets
from gameover import game_over

def salvage(screen, board, player, assets):
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    topbar = font.render("Salvage enemy ships", True, BRIGHT_WHITE)
    smfont = pygame.font.Font(None, 24)
    skip = smfont.render("Skip", True, BRIGHT_RED)
    skip_rect = skip.get_rect()
    choose = smfont.render("Salvage Module", True, BRIGHT_WHITE)
    choose_sel = smfont.render("Salvage Module", True, BRIGHT_GREEN)
    choose_rect = choose.get_rect()
    toprect = topbar.get_rect()
    card_choices = assets.get_cards(3, class_cards=True, neutral_cards=True)
    salvage_box = pygame.Rect((0, 0, SCREEN_WIDTH * (3 / 4), SCREEN_HEIGHT * (3 / 4)))
    salvage_box.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    toprect.centerx = salvage_box.centerx
    toprect.y = salvage_box.y
    for card in card_choices:
        card.rect.center = salvage_box.center
        card.rect.move_ip(0, -50)
    card_choices[0].rect.x -= CARD_WIDTH + 50
    card_choices[2].rect.x += CARD_WIDTH + 50
    skip_rect.midtop = card_choices[0].rect.midbottom
    choose_rect.midtop = card_choices[2].rect.midbottom
    skip_rect.y += 50
    choose_rect.y += 50

    choices = cards.Hand()
    choices.add(*card_choices)
    current_choice = None
    while True:
        board.draw(screen)
        player.draw(screen)
        pygame.time.Clock().tick(40)
        screen.blit(topbar, toprect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if skip_rect.collidepoint(position):
                    return
                elif current_choice and choose_rect.collidepoint(position):
                    player.all_cards.append(current_choice)
                    return
                else:
                    current_choice = None
                    position = pygame.mouse.get_pos()
                    for card in choices:
                        if card.rect.collidepoint(position):
                            card.highlight = not card.highlight
                            if card.highlight:
                                current_choice = card
                        else:
                            card.highlight = False
        screen.blit(skip, skip_rect)
        if current_choice:
            screen.blit(choose_sel, choose_rect)
        else:
            screen.blit(choose, choose_rect)
        choices.draw(screen)
        pygame.display.update()

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
        position = pygame.mouse.get_pos()
        target.update(position)
        #ygame.draw.rect(screen, WHITE, card_area, 1)
        if card.ctype == 'TARGET_ATTACK':
            # changes targeting recticle if a sucessful
            # collisoin with the enemy is detected
            if any([sp.collision(position) for sp in enemy_group]):
                screen.blit(target.get_atk(), position)
            else:
                screen.blit(target.get_img(), position)
        else:
            # non targeted attack
            # highlights targeting recticle if outside card area
            if not card_area.collidepoint(position):
                screen.blit(target.get_bst(), position)
            else:
                screen.blit(target.get_img(), position)

        pygame.event.pump()
        pygame.display.update()
    if card.ctype == 'TARGET_ATTACK':
        targeted = [sp for sp in enemy_group if sp.collision(position)]
        if targeted:
            card.process_card(player, enemy_group)
            ret = True
    else:
        if not card_area.collidepoint(position):
            card.process_card(player, enemy_group)
            ret = True
    pygame.mouse.set_visible(True)
    return ret

def battle(screen, player, assets):
    pygame.font.init()
    board = GameBoard("spacefield_a-000.png")
    enemy_group = EnemyFleet()
    player_turn = True
    # change to dynamically create enemies
    enemy_group.spawn(assets.enemy_choices)

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
    while enemy_group:
        pygame.time.Clock().tick(40)
        # draw background
        board.draw(screen)
        # dynamic hand animation
        player.hand.ddraw(screen, pygame.mouse.get_pos())
        # place the player object (the loaded image)
        player.draw(screen)
        enemy_group.draw(screen)
        if player_turn:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if board.end_turn.collision(mouse_pos):
                        player.end_turn(board)
                        enemy = (e for e in enemy_group.sprites())
                        enemy_group.drain_shields()
                        player_turn = False
                    else:
                        for card in player.hand:
                            if card.rect.collidepoint(mouse_pos):
                                card.highlight = True
                                if targeting(screen, board, card, player, enemy_group):
                                    player.hand.position_hand()
                                card.highlight = False
                                break
                #elif event.type == MOUSEMOTION:
            board.highlight(screen, mouse_pos)
        else:
            # enemies take their turns attacking
            try:
                cur = next(enemy)
                cur.attack(player, assets)
                pygame.time.wait(500)
                if player.dead():
                    return False
            except StopIteration:
                player_turn = True
                player.drain_shields()

        # update the display every iteration of this loop
        pygame.display.update()
    salvage(screen, board, player, assets)
    return True

if __name__ == "__main__":
    # Run battle.py directly to test battle functionality
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # declare the size of the map
    assets = GameAssets()
    player = Player()
    player.move(0, SCREEN_HEIGHT / 3)
    basics = assets.all_cards['basic']
    for _ in range(4):
        player.all_cards.append(basics[0].copy())
        player.all_cards.append(basics[1].copy())
    for _ in range(2):
        player.all_cards.append(assets.all_cards['fighter'][0].copy())
    ret = True
    while ret:
        ret = battle(screen, player, assets)
    game_over(screen)
    pygame.display.quit()
