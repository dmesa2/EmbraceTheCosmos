import random
import pygame
from pygame.locals import *
from gamestate import *
import battle
import escape
from gameassets import GameAssets

def find_money(screen, player, assets, escape_call):
    cash = random.randint(100, 250)
    player.credits += cash
    pygame.font.init()
    bg = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'Background', 'nebula', 'nebula07.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
    large = pygame.font.Font(None, 58)
    event_msg = large.render("You find the wreckage of merchant ship", False, BRIGHT_WHITE)
    event_msg2 = large.render("You salvage {} credits from the ship.".format(cash), False, BRIGHT_WHITE)
    ev1_rect = event_msg.get_rect(midbottom=(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2))
    ev2_rect = event_msg2.get_rect(midtop=ev1_rect.midbottom)
    small = pygame.font.Font(None, 22)
    cont_no = small.render("Continue", False, RED)
    cont_go = small.render("Continue", False, GREEN)
    rect = cont_no.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (2 / 3)))
    screen.blit(bg, (0, 0))
    screen.blit(event_msg, ev1_rect)
    screen.blit(event_msg2, ev2_rect)
    screen.blit(cont_no, rect)
    pygame.display.update()
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
            elif event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(pos):
                    return True
        pygame.display.update()

def events(screen, player, assets, escape_call):
    events = [battle.battle, find_money]
    event_choice = random.choice(events)
    return event_choice(screen, player, assets, escape_call)
