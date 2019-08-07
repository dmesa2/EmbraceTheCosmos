import pygame
from pygame.locals import *
from gamestate import *
import gameassets
from character import Player
import sys
import os
from escape import Escape

def repair(screen, player, assets):
    pygame.font.init()
    bg = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'Background', 'nebula', 'nebula07.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
    large = pygame.font.Font(None, 64)
    repair_msg = large.render("Your ship has repaired 30%", False, BRIGHT_WHITE)
    repair_msg2 = large.render("hull integrity.", False, BRIGHT_WHITE)
    rep1_rect = repair_msg.get_rect(midbottom=(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2))
    rep2_rect = repair_msg2.get_rect(midtop=rep1_rect.midbottom)
    small = pygame.font.Font(None, 22)
    cont_no = small.render("Continue", False, RED)
    cont_go = small.render("Continue", False, GREEN)
    rect = cont_no.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (2 / 3)))
    player_rect = player.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6))
    player.move(player_rect.x, player_rect.y)
    player.current_health += player.current_health * 0.30
    if player.current_health > player.max_health:
        player.current_health = player.max_health
    screen.blit(bg, (0, 0))
    player.draw(screen)
    screen.blit(repair_msg, rep1_rect)
    screen.blit(repair_msg2, rep2_rect)
    screen.blit(cont_no, rect)
    pygame.display.update()
    pygame.time.wait(1000)
    escape_call = Escape()

    while True:
        pygame.time.Clock().tick(40)
        pos = pygame.mouse.get_pos()
        if rect.collidepoint(pos):
            screen.blit(cont_go, rect)
        else:
            screen.blit(cont_no, rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape_call.escape_menu(screen)
                    break

            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(pos):
                    return
        pygame.display.update()

if __name__ == '__main__':
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player()
    repair(screen, player, None)
