import pygame
from gamestate import *
import character
import os
import json
'''
names: grass, zap, bumble, orange
'''
class EnemyChoice:
    def __init__(self):
        path = os.path.join(ASSETS_PATH, 'enemies.json')
        self.groupings = self.groups()
        self.sprite_buffer = self.load_enemies(path)

    def read_enemy(self, sp):
        if sp['name'] == 'boss':
            img = pygame.image.load(os.path.join(ASSETS_PATH, 'Spaceships/spaceships', sp['image_path']))
            ret = character.Enemy(img, sp['max_health'],
            sp['shield'], sp['credits'], sp['attack_pattern'], is_boss=True)
        else:
            img = pygame.image.load(os.path.join(ASSETS_PATH, SHIPS_PATH, sp['image_path']))
            ret = character.Enemy(img, sp['max_health'], sp['shield'], sp['credits'], sp['attack_pattern'], sp['model'])

        return ret

    def load_enemies(self, fname):
        '''
        Returns a dictionary of names : enemy class
        '''
        with open(fname, 'r') as f:
            enemies = json.load(f)
        ret = {e['name'] : self.read_enemy(e) for e in enemies}
        return ret

    def groups(self):
        g = 'grass'
        z = 'zap'
        b = 'bumble'
        o = 'orange'

        enemy_groups = [[z, g],
                        [g, o, g],
                        [b, o, o],
                        [b, o, z],
                        [b, b]]

        return enemy_groups
