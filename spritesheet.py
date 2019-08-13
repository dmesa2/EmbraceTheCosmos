import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
''' 
Modified from pygame tutorial on spritesheets
https://www.pygame.org/wiki/Spritesheet
'''

class Spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA) 
        image.blit(self.sheet, (0, 0), rect)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect) for rect in rects]
    
    # Load a whole strip of images
    def load_strip(self, rect, image_count):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups)


def init():
    pygame.display.init()
    sc = pygame.display.set_mode((800,600))
    return sc


def test(sc):
    sh = Spritesheet("beams.png")
    r1 = (210, 310, 50, 90)
    img = sh.image_at(r1)
    sc.blit(img, (300, 300))
    pygame.display.update()

