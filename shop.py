import pygame
from pygame.locals import *
from gamestate import *
import gameassets
import character
import cards
import escape
import sys
import os

def shop(screen, player, assets, escape_call):
    ncards = 6
    pygame.font.init()
    # Set up icons/fonts to be drawn
    done = pygame.image.load(os.path.join(ICON_PATH, 'button_done-shopping.png'))
    done_rect = done.get_rect(bottomright=(SCREEN_WIDTH, SCREEN_HEIGHT))
    large = pygame.font.Font(None, 64)
    med = pygame.font.Font(None, 32)
    small = pygame.font.Font(None, 16)
    money = pygame.transform.scale(assets.coin, (16, 16))
    black_market = large.render("Hober's Black Market", False, WHITE)
    card_cost = small.render("10 Coins", False, WHITE)
    bm_rect = black_market.get_rect(midtop=(SCREEN_WIDTH / 2, 0))
    cc_rect = card_cost.get_rect(midtop=(SCREEN_WIDTH / 2, 0))
    player_credits = med.render("{} credits".format(player.credits), False, Color("gold"))
    bg = pygame.image.load(os.path.join(BACKGROUND_PATH, 'nebula', 'nebula06.png'))
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Get cards to offer player and add to for_sale group
    sale_cards = assets.get_cards(ncards, True, True)
    for_sale = cards.Hand()
    for_sale.add(*sale_cards)

    # set up positions for cards
    lvl_1 = black_market.get_height() * 1.5
    lvl_2 = lvl_1 + CARD_HEIGHT  + 1 / 8 * CARD_HEIGHT
    px = 1 / 2 * CARD_WIDTH
    x_delta = CARD_WIDTH + 1 / 8 * CARD_WIDTH
    positions = []
    for i in range(ncards // 2):
        positions.append((px, lvl_1))
        positions.append((px, lvl_2))
        px += x_delta

    # update each card with its display position
    for card, pos in zip(for_sale.sprites(), positions):
        card.pos = list(pos)
    for_sale.update()

    while True:
        pygame.time.Clock().tick(40)
        screen.blit(bg, (0, 0))
        screen.blit(done, done_rect)
        screen.blit(black_market, bm_rect)
        screen.blit(player_credits, player_credits.get_rect(bottomleft=(0, SCREEN_HEIGHT)))
        #for_sale.draw(screen)
        for card in for_sale.sprites():
            screen.blit(card.image, card.rect)
            screen.blit(money, card.rect.bottomleft)
            screen.blit(card.price_str, card.rect.midbottom)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if done_rect.collidepoint(pos):
                    return
                else:
                    for_sale.buy_card(player, pos)
                player_credits = med.render("{} credits".format(player.credits), False, Color("gold"))

if __name__=="__main__":
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = character.Player()
    assets = gameassets.GameAssets()
    shop(screen, player, assets)
