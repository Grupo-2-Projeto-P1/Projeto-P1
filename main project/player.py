import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/player_stopped.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_up1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_up1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_up2.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_right.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_right1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_right2.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_left.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_left1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_left2.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_down1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_down2.png'))
        self.stopped = 0
        self.up = 1
        self.right = 4
        self.left = 7
        self.down = 10
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
    def baixo(self, x, y):
        self.image = self.sprites[int(self.atualsul)]
        self.atualsul += 0.2
        if self.atualsul > 12.5:
            self.atualsul = 10
        self.rect.topleft = x, y
    def cima(self, x, y):
        self.image = self.sprites[int(self.atualcima)]
        self.atualcima += 0.2
        if self.atualcima > 4:
            self.atualcima = 1
        self.rect.topleft = x, y
    def direita(self, x, y):
        self.image = self.sprites[int(self.atualdireita)]
        self.atualdireita += 0.2
        if self.atualdireita > 7:
            self.atualdireita = 4
        self.rect.topleft = x, y
    def esquerda(self, x, y):
        self.image = self.sprites[int(self.atualesquerda)]
        self.atualesquerda += 0.2
        if self.atualesquerda > 10:
           self.atualesquerda = 7
        self.rect.topleft = x, y
    def parado(self, x, y):
        self.image = self.sprites[0]
        self.rect.topleft = x, y

    #linha 730
