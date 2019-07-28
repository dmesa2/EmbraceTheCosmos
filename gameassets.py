import pygame
from load_enemies import EnemyChoice
from gamestate import *
import os
import cards
import random

class GameAssets:
    def __init__(self):
        self.enemy_choices = EnemyChoice()
        self.sc_width = SCREEN_WIDTH
        self.sc_height = SCREEN_HEIGHT
        self.all_cards = cards.load_cards(os.path.join(ASSETS_PATH, CARD_PATH, 'cards.json'))
        self.class_cards = self.all_cards['fighter']
        self.neutral_cards = self.all_cards['neutral']
        ec = cards.load_cards(os.path.join(ASSETS_PATH, CARD_PATH, 'enemy_cards.json'))['enemy']
        self.enemy_cards = {e.name : e for e in ec}
        self.coin = pygame.image.load(os.path.join(ICON_PATH, "metal-disc.png"))
    def get_cards(self, ncards, class_cards=False, neutral_cards=False):
        cards = []
        if class_cards:
            cards += self.class_cards
        if neutral_cards:
            cards += self.neutral_cards
        ret = random.sample(cards, ncards)
        ret = [card.copy() for card in ret]
        return ret
