import pygame
from pygame.locals import *
from level import *
from colors import *
from map import *  # Importe a classe Map após level e colors
from sys import exit

pygame.init()

game_running = True

width = 640
height = 640

screen_center = (width / 2, height / 2)
zoom = 1

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teste")
clock = pygame.time.Clock()

# Crie uma instância de Map
map = Map(screen)

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
    screen.fill((0, 0, 0))

    player = pygame.draw.rect(screen, (232, 123, 123), (screen_center[0] - 20, screen_center[1] - 20, 20 * zoom, 20 * zoom))
    map.update(player)

    # desenhando o placar

    pygame.draw.rect(screen, (120, 120, 120), (0, height - 40, width, 40))

    dist = 170
    pos = 10

    pygame.draw.rect(screen, red, (10 + dist * 0, height - 27, 20, 20))
    desenhar_texto(f"({map.collected['r']}/{map.symbols_collectibles['r']})", 30, white, 35, height - 27)

    pygame.draw.rect(screen, green, (10 + dist * 1, height - 27, 20, 20))
    desenhar_texto(f"({map.collected['g']}/{map.symbols_collectibles['g']})", 30, white, 35 + dist * 1, height - 27)

    pygame.draw.rect(screen, blue, (10 + dist * 2, height - 27, 20, 20))
    desenhar_texto(f"({map.collected['b']}/{map.symbols_collectibles['b']})", 30, white, 35 + dist * 2, height - 27)

    pygame.draw.rect(screen, yellow, (10 + dist * 3, height - 27, 20, 20))
    desenhar_texto(f"({map.collected['y']}/{map.symbols_collectibles['y']})", 30, white, 35 + dist * 3, height - 27)

    clock.tick(30)
    pygame.display.update()
