import pygame
from pygame.locals import *
from map import *
from sys import exit
from level import *
from colors import *
from player import Player

pygame.init()

game_running = True

width = 640
height = 640

screen_center = (width / 2, height / 2)
zoom = 1

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pedro: The God of Math")
clock = pygame.time.Clock()

map = Map(screen)

player = Player(307, 298) 
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# prevenindo contra erro de quantidade de coletáveis
if map.works:
  play = True

else:
  play = False
  print("\n\nSe liga pq falhou:\n")
  print("Não tem espaço para todos esses coletáveis no labirinto.\n\nVá com calma :)\n\nDiminua a quantidade de coletáveis que dá certo.\n\n")

def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(texto, True, cor)
    screen.blit(texto, (x, y))

while game_running and play:
  screen.fill((0,0,0))      

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
  all_sprites.draw(screen)
  all_sprites.update()
  map.update(player)
  
  # desenhando o placar
  pygame.draw.rect(screen,(120,120,120),(0,height-40,width,40))

  #dist = 170
  #pos = 10

  pygame.draw.rect(screen,red,(10,height-27,20,20))
  desenhar_texto(f"({map.collected['r']}/{map.symbols_collectibles['r']})",30,white,35,height-27)
  
  pygame.draw.rect(screen,green,(10+150*1,height-27,20,20))
  desenhar_texto(f"({map.collected['g']}/{map.symbols_collectibles['g']})",30,white,35+150*1,height-27)
  
  pygame.draw.rect(screen,blue,(10+150*2,height-27,20,20))
  desenhar_texto(f"({map.collected['b']}/{map.symbols_collectibles['b']})",30,white,35+150*2,height-27)
  
  pygame.draw.rect(screen,yellow,(10+150*3,height-27,20,20))
  desenhar_texto(f"({map.collected['y']}/{map.symbols_collectibles['y']})",30,white,35+150*3,height-27)

  # condição para verificar vitória
  if map.reached_exit and sum(map.collected.values()) == map.total_objects:
      desenhar_texto("Parabens, você coletou todos os objetos e encontrou a saída! Você venceu!", 48, (255, 255, 255), width // 2 - 100, height // 2 - 50)


  clock.tick(30)
  pygame.display.update()
