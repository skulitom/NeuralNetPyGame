import pygame ,sys , random

from pygame.locals import *
from Variables import *
from Player import Player, Bullet
from random import randrange
from Npc import Enemy

class mainGame:

    score = 0
    endGame = False

    def start(self):
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(GAME_SIZE)
        pygame.display.set_caption(GAME_NAME+" "+VERSION)
        self.DISPLAYSURF.fill(WHITE)
        self.background = pygame.Surface(self.DISPLAYSURF.get_size())
        self.background = self.background.convert()
        self.background.fill(WHITE)
        self.DISPLAYSURF.blit(self.background, (0,0))
        self.player = Player()
        self.allSpriteList = pygame.sprite.Group()
        self.bulletList = pygame.sprite.Group()
        self.enemyList = pygame.sprite.Group()
        self.allSpriteList.add(self.player)
        self.playerSprite = pygame.sprite.RenderPlain(self.player)
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        while not self.endGame:
            self.checkEvents()
            self.checkLocations()
            self.spawnEnemy()
            self.attackPlayer()
            pygame.display.update()
            self.DISPLAYSURF.blit(self.background, (0, 0))
            self.allSpriteList.update()
            self.allSpriteList.draw(self.DISPLAYSURF)
            self.playerSprite.update()
            self.clock.tick(60)

    def checkLocations(self):
        for bullet in self.bulletList:
            hitList = pygame.sprite.spritecollide(bullet, self.enemyList, True)

            for enemy in hitList:
                self.bulletList.remove(bullet)
                self.allSpriteList.remove(bullet)
                self.enemyList.remove(enemy)
                self.allSpriteList.remove(enemy)
                self.score+=1
            if bullet.rect.y < -10:
                self.bulletList.remove(bullet)
                self.allSpriteList.remove(bullet)

        if pygame.sprite.spritecollide(self.player, self.enemyList, True):
                self.endGame=True

    def attackPlayer(self):
        for enemy in self.enemyList:
            enemy.attack(self.player.rect.x,self.player.rect.y)

    def spawnEnemy(self):
        randomNum = randrange(1,50)
        if randomNum == 1:
            randomPos = randrange(1,399)
            enemy = Enemy()
            enemy.rect.x = randomPos
            enemy.rect.y = 0
            self.enemyList.add(enemy)
            self.allSpriteList.add(enemy)

    def checkEvents(self):
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_UP]:
            self.player.move(0,-5)
        if keys[pygame.K_DOWN]:
            self.player.move(0, 5)
        if keys[pygame.K_LEFT]:
            self.player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(5, 0)
        if keys[pygame.K_SPACE]:
            bullet = Bullet()
            bullet.rect.x = self.player.rect.x+25
            bullet.rect.y = self.player.rect.y
            self.allSpriteList.add(bullet)
            self.bulletList.add(bullet)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


