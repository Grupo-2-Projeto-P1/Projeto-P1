import pygame
import random

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

class Collectible:
    def __init__(self, id):
        self.rect = pygame.Rect(0,0,20,20) # um quadrado dele
        self.id = id                       # pode ser r g b y
        self.collected = False             # se foi coletado
        self.pos_x = int()                 # o indice dele na linha da matriz
        self.pos_y = int()                 # o indice dele na coluna da matriz
        self.color = tuple()               # a cor dele mesmo

        match self.id:
            case 'r': # quadrante superior esquerdo
                self.pos_x = random.choice(range(0,6))
                self.pos_y = random.choice(range(0,6))
                self.color = red
            
            case 'g': # quadrante superior direito
                self.pos_x = random.choice(range(7,14))
                self.pos_y = random.choice(range(0,6))
                self.color = green
            
            case 'b': # quadrante inferior esquerdo
                self.pos_x = random.choice(range(0,6))
                self.pos_y = random.choice(range(7,14))
                self.color = blue

            case 'y': # quadrante inferior direito
                self.pos_x = random.choice(range(7,14))
                self.pos_y = random.choice(range(7,14))
                self.color = yellow
