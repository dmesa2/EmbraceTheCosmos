import pygame
from pygame.locals import *
from gamestate import *
import gameassets
import character
import cards
import sys

def shop(screen, player, assets):
    ncards = 6
    pygame.font.init()
    large = pygame.font.Font(None, 64)
    small = pygame.font.Font(None, 16)
    money = pygame.transform.scale(assets.coin, (16, 16))
    black_market = large.render("Hober's Black Market", False, WHITE)
    bm_rect = black_market.get_rect(midtop=(SCREEN_WIDTH / 2, 0))
    bg = pygame.image.load(os.path.join(BACKGROUND_PATH, 'nebula', 'nebula06.png'))
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    sale_cards = assets.get_cards(ncards, True, True)
    for_sale = cards.Hand()
    for_sale.add(*sale_cards)
    lvl_1 = black_market.get_height() * 1.5
    lvl_2 = lvl_1 + CARD_HEIGHT  + 1 / 8 * CARD_HEIGHT
    px = 1 / 2 * CARD_WIDTH
    x_delta = CARD_WIDTH + 1 / 8 * CARD_WIDTH
    positions = []
    for i in range(ncards // 2):
        positions.append((px, lvl_1))
        positions.append((px, lvl_2))
        px += x_delta
    for card, pos in zip(for_sale.sprites(), positions):
        print(card.name, pos)
        card.pos = list(pos)
    for_sale.update()
    while True:
        pygame.time.Clock().tick(40)
        screen.blit(bg, (0, 0))
        screen.blit(black_market, bm_rect)
        #for_sale.draw(screen)
        for card in for_sale.sprites():
            screen.blit(card.image, card.rect)
            screen.blit(money, card.rect.bottomleft)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__=="__main__":
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = character.Player()
    assets = gameassets.GameAssets()
    shop(screen, player, assets)
