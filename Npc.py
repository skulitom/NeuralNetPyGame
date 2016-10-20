import pygame

from pygame import *
from Variables import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(ENEMY_SIZE)
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def attack(self,x,y):
        if x > self.rect.x:
            self.rect.x+=ENEMY_SPEED
        else:
            self.rect.x-=ENEMY_SPEED
        if y > self.rect.y:
            self.rect.y+=ENEMY_SPEED
        else:
            self.rect.y-=ENEMY_SPEED