import pygame
from button import Button

pygame.init()

# Tamanho da tela 
WIDTH = 800
HEIGHT = 700 

# Definição do tamanho da tela e definição do background
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Cria uma tela e determina o seu tamanho
bg_img = pygame.image.load('../assets/images/main_background.png')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

# Fonte 
font = pygame.font.Font('../assets/font\Pixeled.ttf', 20)

def write_text(text_content, font, color, pos_x, pos_y): # Função para escrever texto na tela 
    text = font.render(text_content, True, color)
    screen.blit(text, (pos_x, pos_y))

def instructions_screen(): # A tela de instruções
    # Imagem de Background
    instructions_screen_bg = pygame.image.load('../assets\images\help_screen.png')
    instructions_screen_bg = pygame.transform.scale(instructions_screen_bg,(WIDTH,HEIGHT))
    
    pygame.display.set_caption("Pedro: God of the Math") # Coloca o nome do jogo
    # Título e Ícone
    icon = pygame.image.load('../assets\images\icon.png')
    pygame.display.set_icon(icon)
    
    #Fonte
    text_font = pygame.font.Font('../assets/font\Pixeled.ttf', 15)
    tittle_font = pygame.font.Font('../assets/font\Pixeled.ttf', 30)

    while True:
        screen.blit(instructions_screen_bg, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load("../assets\images\exit_icon.png")
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (30, 30))

        QUIT_BUTTON = Button(BUTTON_IMAGE, 700, 87, font, "")
        QUIT_BUTTON.update(screen)
        

        
        STRING_LIST = ["O objetivo do jogo é passar pelo labirinto", "coletando os itens dispostos no mapa.", "Para jogar, utilize as teclas W A S D para movi-", "mentar o personagem. Divirta-se :)"] 
        initial_x = 110
        initial_y = 150
        
        write_text("INSTRUÇOES", tittle_font, (0,0,0), 110, 80)

        for line in STRING_LIST:
            write_text(line, text_font, (0,0,0), initial_x, initial_y)
            initial_y += 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.clicked(mouse_pos):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Pedro: God of the Math") # Coloca o nome do jogo
    # Título e Ícone
    icon = pygame.image.load('../assets\images\icon.png')
    pygame.display.set_icon(icon)
    
    while True:
        screen.blit(bg_img, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        BUTTONS_LIST = []

        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load("../assets\images\start_button.png")
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (251, 81))

        # Botão de iniciar o jogo
        START_BUTTON = Button(BUTTON_IMAGE, 200, 500, font, "INICIAR")
        BUTTONS_LIST.append(START_BUTTON)
        
        # Botão de fechar o jogo
        INSTRUCTIONS_BUTTON = Button(BUTTON_IMAGE, 600, 500, font, "INSTRUÇOES")
        BUTTONS_LIST.append(INSTRUCTIONS_BUTTON)
        
        for i in BUTTONS_LIST:
            i.interaction_text_color(mouse_pos)
            i.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.clicked(mouse_pos):
                    print("Clicado")
                if INSTRUCTIONS_BUTTON.clicked(mouse_pos):
                    instructions_screen()

        pygame.display.update()

