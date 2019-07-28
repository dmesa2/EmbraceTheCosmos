import pygame
from gamestate import *

class Button(pygame.sprite.Sprite):
    def __init__(self, image, image_alt, x, y, rescale_factor=None):
        super().__init__()
        self.image = pygame.image.load(os.path.join(ASSETS_PATH, 'Misc', image))
        self.image_alt = pygame.image.load(os.path.join(ASSETS_PATH, 'Misc', image_alt))
        if rescale_factor:
            self.image = pygame.transform.scale(self.image, rescale_factor)
            self.image_alt = pygame.transform.scale(self.image_alt, rescale_factor)
        self.rect = self.image.get_rect(topleft = (x, y))

    def draw(self, screen, alt=None):
        if alt:
            screen.blit(self.image_alt, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def _draw_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)

    def collision(self, position):
        return self.rect.collidepoint(position)

class GameBoard:
    def __init__(self, bg_img):
        self.background = pygame.transform.scale(pygame.image.load(
                os.path.join(ASSETS_PATH, "Background", bg_img)),
                (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end_turn = Button('end_turn.png', 'end_turn_alt.png',
                SCREEN_WIDTH - 48, SCREEN_HEIGHT - 48, (48, 48))
        self.deck = Button('deck_icon.png', 'deck_icon_alt.png',
                24, SCREEN_HEIGHT - 72 - 48, (48, 48))
        self.graveyard = Button('pirate-grave.png', 'pirate-grave_alt.png',
                24, SCREEN_HEIGHT - 72, (48, 48))

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.end_turn.draw(screen)
        self.deck.draw(screen)
        self.graveyard.draw(screen)

    def _show_boxes(self, screen):
        self.end_turn._draw_box(screen)
        self.graveyard._draw_box(screen)
        self.deck._draw_box(screen)

    def highlight(self, screen, position, alwayson):
        if alwayson or self.end_turn.rect.collidepoint(position):
            self.end_turn.draw(screen, True)
        elif self.deck.rect.collidepoint(position):
            self.deck.draw(screen, True)
        elif self.graveyard.rect.collidepoint(position):
            self.graveyard.draw(screen, True)
