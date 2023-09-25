import pygame
import random

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
purple = (120,0,120)
orange = (255,94,5)
white = (255,255,255)

# color_k = {'r':red,'R':red,'g':green,'G':green,'b':blue,'B':blue,'y':yellow,'p':purple,'o':orange}

color_k = {'r':red,'g':green,'b':blue,'y':yellow,'p':purple,'O':orange}

class Collectible:
    def __init__(self, id):
        self.rect = pygame.Rect(0,0,20,20) # um quadrado dele
        self.id = id                       # pode ser r g b y
        self.collected = False             # se foi coletado
        self.pos_x = int()                 # o indice dele na linha da matriz
        self.pos_y = int()                 # o indice dele na coluna da matriz
        self.color = color_k[id]      # a cor dele mesmo
        self.collected_string = "Não coletado"
        

        if self.id in ['r','p']: # quadrante superior esquerdo
            self.pos_x = random.choice(range(0,6))
            self.pos_y = random.choice(range(0,6))
            
        
        elif self.id in ['g', 'G']: # quadrante superior direito
            self.pos_x = random.choice(range(7,14))
            self.pos_y = random.choice(range(0,6))
        
        elif self.id in ['b', 'B']: # quadrante inferior esquerdo
            self.pos_x = random.choice(range(0,6))
            self.pos_y = random.choice(range(7,14))

        elif self.id in ['y', 'O']: # quadrante inferior direito
            self.pos_x = random.choice(range(7,14))
            self.pos_y = random.choice(range(7,14))

        else:
            self.pos_x = random.choice(range(0,14))
            self.pos_y = random.choice(range(0,14))
        
        print(self.color)
