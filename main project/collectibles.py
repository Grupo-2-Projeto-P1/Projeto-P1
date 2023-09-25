import pygame
from random import choice
from colors import *

color_k = {'r': red, 'g': green, 'b': blue, 'y': yellow}

class Collectible:
    def __init__(self, id):
        self.rect = pygame.Rect(0,0,20,20) # um quadrado dele
        self.id = id                       # pode ser r g b y
        self.collected = False             # se foi coletado
        self.coords = list()
        self.color = color_k[id]           # a cor dele mesmo
        self.collected_string = "Não coletado"

        self.take_interval(self.id)
        self.pos_x = self.coords[0]                 # o indice dele na linha da matriz
        self.pos_y = self.coords[1]                 # o indice dele na coluna da matriz
    
    def take_interval(self, id):
        range0_6 = range(0,6)
        range7_14 = range(7,14)

        if id == "r": self.coords = [choice(range0_6), choice(range0_6)]
        if id == "g": self.coords = [choice(range7_14), choice(range0_6)]
        if id == "b": self.coords = [choice(range0_6), choice(range7_14)]
        if id == "y": self.coords = [choice(range7_14), choice(range7_14)]
