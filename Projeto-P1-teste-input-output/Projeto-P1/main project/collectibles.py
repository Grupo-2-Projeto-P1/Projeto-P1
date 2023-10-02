import pygame
import random
from colors import *

# Para escolher a quantidade de coletáveis, vá em map
# Modifique os números no dicionário symbols_collectibles

class Collectible():
  def __init__(self, item):
    self.item = item
    self.all_collectibles = list()
    self.rect = pygame.Rect(0,0, 0, 0)
    self.collected = False

    if item == "r": 
      self.color = red
      self.name = "Vermelho"
    if item == "g": 
      self.color = green
      self.name = "Verde"
    if item == "b": 
      self.color = blue
      self.name = "Azul"
    if item == "y": 
      self.color = yellow
      self.name = "Amarelo"

    self.row = random.choice(range(0,14))
    self.column = random.choice(range(0,14))

    self.adress = (self.row,self.column)
