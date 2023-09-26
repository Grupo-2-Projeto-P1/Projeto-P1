import pygame
from button import Button

pygame.init()

# Tamanho da tela 
WIDTH = 900 
HEIGHT = 600 

# Música e efeitos sonoros 
pygame.mixer.music.load('../assets/sounds/Soundtrack_menu.mp3') # Música de Background 
pygame.mixer.music.play() 

CLICK_SOUND = pygame.mixer.Sound('../assets/sounds/clicked_sound.mp3') # Efeito sonoro de click

# Definição do tamanho da tela e definição do background
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Cria uma tela e determina o seu tamanho
bg_img = pygame.image.load('../assets/images/main_background.png')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

# Fonte 
font_path = '../assets/font\Pixeled.ttf'
font = pygame.font.Font(font_path, 20)

def write_text(text_content, font_path, color, pos_x, pos_y, font_size): # Função para escrever texto na tela 
    font = pygame.font.Font(font_path, font_size)
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
        
        write_text("INSTRUÇOES", font_path, (0,0,0), 110, 80, 30)

        # Loop criado para printar cada string para simular a quebra de linha
        for line in STRING_LIST:
            write_text(line, font_path, (0,0,0), initial_x, initial_y, 15)
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
    
    muted = False # Variável para detectar se a música encontra-se mutada
    button_image_path = "../assets\images\start_button.png"
    button_image_music_path = "../assets\images\music_icon.png"
    
    while True:
        screen.blit(bg_img, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        buttons_list = []

        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load(button_image_path)
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (251, 81))

        # Imagem do ícone do botão da Música
        BUTTON_IMAGE_MUSIC = pygame.image.load(button_image_music_path)
        BUTTON_IMAGE_MUSIC = pygame.transform.scale(BUTTON_IMAGE_MUSIC, (41, 41))

        # Botão de iniciar o jogo
        START_BUTTON = Button(BUTTON_IMAGE, 200, 500, font, "INICIAR")
        buttons_list.append(START_BUTTON)
        
        # Botão de fechar o jogo
        INSTRUCTIONS_BUTTON = Button(BUTTON_IMAGE, 600, 500, font, "INSTRUÇOES")
        buttons_list.append(INSTRUCTIONS_BUTTON)

        # Botão de mutar a música
        MUSIC_BUTTON = Button(BUTTON_IMAGE_MUSIC, 30, 30, font, "")
        buttons_list.append(MUSIC_BUTTON)
        
        for i in buttons_list:
            i.interaction_text(mouse_pos)
            i.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.clicked(mouse_pos):
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    print("Clicado")
                if INSTRUCTIONS_BUTTON.clicked(mouse_pos):
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    instructions_screen()
                if MUSIC_BUTTON.clicked(mouse_pos):
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    if muted == False: 
                        muted = True
                        button_image_music_path = "../assets\images\muted_music_icon.png"
                        pygame.mixer.music.pause()
                    else: # muted == True
                        muted = False 
                        button_image_music_path = "../assets\images\music_icon.png"
                        pygame.mixer.music.unpause()

        pygame.display.update()

