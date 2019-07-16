import pygame
from gamestate import *
import character
import os

def read_enemies(sp):
    img = os.path.join(ASSETS_PATH, SHIPS_PATH, sp['image'])
    ret = character.Enemy(img, sp['max_health'],
        sp['shield'], sp['attack_pattern'])

def load_enemies(fname):
    with open(fname, 'r') as f:
        enemies = json.load(f)
    ret = [read_enemy(e) for e in enemies]
    return ret
