import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import sprite
import random
import cards
from gamestate import *

X = 0
Y = 1

class EnemyFleet(sprite.Group):
    def __init__(self):
        super().__init__()

    def draw_rect(self, screen):
        for s in self.sprites():
            s.show_box(screen)

    def draw(self, screen):
        for sp in self.sprites():
            sp.draw(screen)

    def process_attack(self, card, target=None):
        if target:
            target.damage(card.damage)
        else:
            for sp in self.sprites():
                sp.damage(card.damage)

    def dead(self, screen, board, player, enemy_group):
        for sp in self.sprites():
            sp.dead(screen, board, player, enemy_group)

    def spawn(self, ec):
        group = random.choice(ec.groupings)
        for sp in group:
            self.add(ec.sprite_buffer[sp].copy())
        self.place()

    def place(self):
        coords = [(450, 250),
                  (550, 150),
                  (650, 50),
                  (550, 350),
                  (650, 450)]
        for pos, sp in zip(coords, self.sprites()):
            sp.move(pos[0], pos[1])

    def drain_shields(self):
        for sp in self.sprites():
            sp.drain_shields()

class Character(sprite.Sprite):
    def __init__(self, img_path=None, image=None, explosion_path=None,
                explosions=None, max_health=40, credits=0):
        super().__init__()
        if img_path:
            self.image = pygame.image.load(img_path)
        else:
            self.image = image
        if explosion_path:
            path = os.path.join(EXPLOSIONS_PATH, explosion_path + '_Explosion')
            imgs = list(os.scandir(path))
            self.explosions = [pygame.image.load(png.path).convert_alpha() for png in imgs]
        else:
            self.explosions = explosions
        self.pos = [0, 0]
        self.rect = self.image.get_rect(topleft=self.pos)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.health_bar = self.health_init()
        # stats
        self.max_health = max_health
        self.current_health = max_health
        self.shield = 0
        self.credits = credits

    def update(self):
        self.rect = self.image.get_rect(topleft=self.pos)
        self.bounding_rect = self.image.get_bounding_rect()
        self.bounding_rect.center = self.rect.center
        self.health_init()

    def health_init(self):
        left, top, width, height = self.bounding_rect
        self.health_bar = pygame.Rect((left, top + height, width, 8))

    def collision(self, position):
        return self.bounding_rect.collidepoint(position)

    def rescale(self, w, h):
        self.image = pygame.transform.scale(self.image, (w, h))

    def rescale_factor(self, n):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * n, height * n))
        self.update()

    def copy(self):
        return Character(image=self.image)

    def move(self, x, y):
        self.pos = [x, y]
        self.update()

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def get_img(self):
        return self.image

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.bounding_rect, 1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        font = pygame.font.Font(None, 16)
        if self.max_health > 0:
            if self.shield:
                pygame.draw.rect(screen, BLUE, self.health_bar)
                val = font.render(str(self.shield), True, YELLOW)
                valr = val.get_rect(center=self.health_bar.center)
            else:
                pygame.draw.rect(screen, GRAY, self.health_bar)
                health = self.health_bar.copy()
                health.width *= self.current_health / self.max_health
                pygame.draw.rect(screen, RED, health)
                val = font.render("{} / {}".format(self.current_health, self.max_health), True, YELLOW)
                valr = val.get_rect(center=self.health_bar.center)
            screen.blit(val, valr)

    def damage(self, ndmg):
        if self.shield:
            if self.shield > ndmg:
                self.shield -= ndmg
            else:
                ndmg -= self.shield
                self.shield = 0
                self.current_health -= ndmg
        else:
            self.current_health -= ndmg
        self.current_health = max(0, self.current_health)

    def drain_shields(self):
        self.shield = 0

    def explode(self, screen, board, player, enemy_group):
        board.draw(screen, player.power, player.max_power)
        player.hand.draw(screen)
        player.draw(screen)
        enemy_group.draw(screen)
        if self in enemy_group:
            self.remove(self.groups())
        pygame.display.update()
        for boom in self.explosions:
            rect = boom.get_rect(center=self.rect.center)
            screen.blit(boom, rect)
            pygame.display.update()
            pygame.time.wait(150)

class Player(Character):
    def __init__(self,
                img_path=os.path.join(SHIPS_PATH, 'Ship3/Ship3.png'),
                ctype='fighter', health=40, power=3, hand=3):
        super().__init__(img_path=img_path, max_health=health, explosion_path='Ship3')
        self.max_handsize = hand
        self.max_power = power
        self.power = 0
        # all cards in the players current deck
        self.all_cards = []
        # player class
        self.ctype = ctype
        # battle hands
        self.hand = cards.Hand()
        self.graveyard = []
        self.deck = []
        self.in_play = []

    def draw_hand(self):
        for _ in range(self.max_handsize):
            # If deck is empty reshuffle graveyard into deck before drawing cards
            if not self.deck:
                random.shuffle(self.graveyard)
                self.deck = self.graveyard.copy()
                self.graveyard = []
            c = self.deck.pop()
            self.hand.add(c)

    def reset_decks(self):
        self.hand.empty()
        self.deck = self.all_cards.copy()
        random.shuffle(self.deck)
        self.graveyard = []
        self.in_play = []

    def end_turn(self, board):
        for card in self.hand:
            self.graveyard.append(card)
            card.remove(self.hand)
        self.draw_hand()
        self.hand.position_hand()

    def dead(self, screen, board, player, enemy_group):
        if self.current_health <= 0:
            self.explode(screen, board, player, enemy_group)
            return True
        return False

class Enemy(Character):
    def __init__(self, image, health, shield, credits, atk_pattern, explosion_path=None, explosions=None):
        super().__init__(image=image, credits=credits, max_health=health, explosion_path=explosion_path, explosions=explosions)
        self.shield = shield
        self.attacks = atk_pattern
        self.attack_idx = 0

    def dead(self, screen, board, player, enemy_group):
        if self.current_health <= 0:
            self.explode(screen, board, player, enemy_group)


    def attack(self, player, assets):
        card = assets.enemy_cards[self.attacks[self.attack_idx]]
        if card.ctype == "BOOST":
            self.shield += card.shield
        elif card.ctype == "TARGET_ATTACK":
            player.damage(card.damage)
        self.attack_idx = (self.attack_idx + 1) % len(self.attacks)


    def copy(self):
        return Enemy(self.image, self.max_health, self.shield, self.credits, self.attacks, explosions=self.explosions)

class Target(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Misc/red_target.png"), TARGET_SIZE)
        self.attack_img = pygame.transform.scale(pygame.image.load("assets/Misc/green_target.png"), TARGET_SIZE)
        self.boost_img = pygame.transform.scale(pygame.image.load("assets/Misc/blue_target.png"), TARGET_SIZE)
        self.rect = self.image.get_rect()

    def update(self, position):
        self.rect = self.image.get_rect(topleft=position)

    def get_img(self):
        return self.image

    def get_atk(self):
        return self.attack_img

    def get_bst(self):
        return self.boost_img

    def show_box(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)
