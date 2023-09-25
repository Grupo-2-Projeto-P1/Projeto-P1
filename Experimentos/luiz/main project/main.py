import pygame
from pygame.locals import *
from map import *
from sys import exit
from level import *

pygame.init()

game_running = True

width = 640
height = 640

screen_center = (width / 2, height / 2)
zoom = 1

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Teste")
clock = pygame.time.Clock()

map = Map(screen)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
purple = (120,0,120)
orange = (255,94,5)
white = (255,255,255)
gray = (120,120,120)

color_k = {'r':red,'g':green,'b':blue,'y':yellow,'p':purple,'O':orange,'w':white}

num_x = 540
num_y = 610

diferenca = 40
primeiro = num_x - 530

text_x = {}
text_y = {}

i = 0
for c in color_k.keys():
  text_x.update({c:primeiro+diferenca*i})
  text_y.update({c:num_y})
  i+= 1

def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(texto, True, cor)
    screen.blit(texto, (x, y))

def mostrar_placar():
  if map.all_collectibles['r'].collected and map.all_collectibles['g'].collected and map.all_collectibles['b'].collected and map.all_collectibles['r'].collected:
    pygame.draw.rect(screen,gray,(0,0,560,75))
    desenhar_texto("Parabéns, você zerou o jogo!", 30, white, 10, 10)
    desenhar_texto("Você coletou todos os itens", 30, white, 10, 50)

  pygame.draw.rect(screen,gray,(0,640-80,640,80))
  
  desenhar_texto("itens coletados:", 30, white, 10, 610-40)

  for c in color_k.keys():
    if map.all_collectibles[c].collected:
      # pygame.draw.rect(screen,color_k[c],(text_x[c],text_y[c],20,20))
      pygame.draw.rect(screen,color_k[c],(text_x[c],text_y[c],20,20))
        
while game_running:
  screen.fill((0,0,0))      

  player = pygame.draw.rect(screen, (232,123,123), (screen_center[0] - 20, screen_center[1] - 20,20*zoom,20*zoom))  
  map.update(player)
  
  mostrar_placar()

  clock.tick(30)
  pygame.display.update()

