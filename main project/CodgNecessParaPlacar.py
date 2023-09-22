# parte a ser colocada na def __init__ de Collectible:
"""
self.collected_string = "Não coletado"
"""
# parte a ser colocada em map na parte que o colle já colidiu:
"""
colle.collected_string = "Coletado"
"""
# parte a ser colocada na main logo antes (acima) do while principal do jogo:
"""
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
white = (255,255,255)
gray = (120,120,120)

def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(texto, True, cor)
    screen.blit(texto, (x, y))

def mostrar_placar():
  if map.all_collectibles['r'].collected and map.all_collectibles['g'].collected and map.all_collectibles['b'].collected and map.all_collectibles['r'].collected:
    pygame.draw.rect(screen,gray,(0,0,560,75))
    desenhar_texto("Parabéns, você zerou o jogo!", 30, white, 10, 10)
    desenhar_texto("Você coletou os itens: Vermelho Verde Azul Amarelo.", 30, white, 10, 50)

  else:
    pygame.draw.rect(screen,gray,(0,640-80,640,80))
    
    num_x = 540
    num_y = 610

    diferenca = 165
    primeiro = num_x - 530

    text_x = {'r':primeiro,'g':primeiro+diferenca,'b':primeiro+2*diferenca,'y':primeiro+3*diferenca}
    text_y = {'r':num_y,'g':num_y,'b':num_y,'y':num_y}

    desenhar_texto("Vermelho:", 30, red, text_x['r'], text_y['r']-30)
    desenhar_texto(f"{map.all_collectibles['r'].collected_string}", 30, white, text_x['r'], text_y['r'])

    desenhar_texto("Verde:", 30, green, text_x['g'], text_y['g']-30)
    desenhar_texto(f"{map.all_collectibles['g'].collected_string}", 30, white, text_x['g'], text_y['g'])

    desenhar_texto("Azul:", 30, blue, text_x['b'], text_y['b']-30)
    desenhar_texto(f"{map.all_collectibles['b'].collected_string}", 30, white, text_x['b'], text_y['b'])

    desenhar_texto("Amarelo:", 30, yellow, text_x['y'], text_y['y']-30)
    desenhar_texto(f"{map.all_collectibles['y'].collected_string}", 30, white, text_x['y'], text_y['y'])
    """
#