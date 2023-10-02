import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/player_stopped.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_up.png'))
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
        self.current_sprite = 0
        self.current_up = 1
        self.current_right = 4
        self.current_left = 7
        self.current_down = 10
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (12*2, 21*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 307, 298


    def baixo(self, x, y):
        self.image = self.sprites[int(self.current_down)]
        self.current_down += 0.25       
        if self.current_down > 12.2:
            self.current_down = 10
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (12*2, 21*2)) 

    def cima(self, x, y):
        self.image = self.sprites[int(self.current_up)]
        self.current_up += 0.25       
        if self.current_up >= 4:
            self.current_up = 1
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (12*2, 21*2))  

    def direita(self, x, y):
        self.image = self.sprites[int(self.current_right)] 
        self.current_right += 0.25        
        if self.current_right >= 7:
            self.current_right = 4
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (12*2, 21*2))  

    def esquerda(self, x, y):
        self.image = self.sprites[int(self.current_left)]   
        self.current_left += 0.25      
        if self.current_left >= 10:
            self.current_left = 7
        self.rect.topleft = x, y 
        self.image = pygame.transform.scale(self.image, (12*2, 21*2))           
    def parado(self, x, y):
        self.image = self.sprites[0]
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (13*2, 22*2))
def player_movement(player):
    keys = pygame.key.get_pressed()
    if keys[K_w] or keys[K_s]:
        if keys[K_w]:
            player.cima(307, 298)
        if keys[K_s]:
            player.baixo(307, 298)

    if keys[K_a] or keys[K_d]:
        if keys[K_a]:
            player.esquerda(307, 298)
        if keys[K_d]:
            player.direita(307, 298)