import pygame

from pygame import *
from Variables import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.speed = SPEED
        self.state = STATE
        self.rect.x = 100
        self.rect.y = 100


    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Bullet(pygame.sprite.Sprite):
    #class for the bullets
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BULLET_SIZE)
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3

