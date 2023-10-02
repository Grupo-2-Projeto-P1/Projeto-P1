class Button():
    # Atributos
    def __init__(self, image, pos_x, pos_y, font, text_content) :
        # Atributos da posição que vai estar
        self.pos_x = pos_x # A posição em relação ao X
        self.pos_y = pos_y # A posição em relação ao Y 
        
        # Atributos da imagem (e da formação do seu "retângulo")
        self.image = image # A imagem do Botão 
        self.image_rect = self.image.get_rect(center=(self.pos_x, self.pos_y)) # A formação do retângulo com as coordenadas
        
        # Atributos do texto dentro da imagem (e também da formação do seu "retângulo")
        self.text_content = text_content # O conteúdo do texto
        self.font = font
        self.text = self.font.render(self.text_content, True, "black")
        self.text_rect = self.text.get_rect(center=(self.pos_x, self.pos_y))
    
    # Função feita para colocar a imagem e o texto e os seus respectivos retângulos (semelhante ao blit colocado para colocar o background)
    def update(self, screen): 
        screen.blit(self.image, self.image_rect) 
        screen.blit(self.text, self.text_rect)

    # Função para detectar se o botão foi clicado
    def clicked(self, position): # O parâmetro position se refere a posição do mouse 
        position_x = position[0] # A posição x é o primeiro elemento da tupla
        position_y = position[1] # A posição y é o segundo elemento da tupla
        if position_x in range(self.image_rect.left , self.image_rect.right) and position_y in range(self.image_rect.top, self.image_rect.bottom):
            return True
        return False
    
    # Função para detectar se o mouse está em cima e mudar a cor do texto (dar sensação de que está sendo reconhecido)
    def interaction_text_color(self, position): 
        position_x = position[0] # A posição x é o primeiro elemento da tupla
        position_y = position[1] # A posição y é o segundo elemento da tupla
        if position_x in range(self.image_rect.left , self.image_rect.right) and position_y in range(self.image_rect.top, self.image_rect.bottom):
            self.text = self.font.render(self.text_content, True, "white")
        # Verificar se esse else tem necessidade
        else:
            self.text = self.font.render(self.text_content, True, "black") 