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

    def get_cards(self, ncards, class_cards=False, neutral_cards=False):
        cards = []
        if class_cards:
            cards += self.class_cards
        if neutral_cards:
            cards += self.neutral_cards
        return random.choices(cards, k=ncards)
