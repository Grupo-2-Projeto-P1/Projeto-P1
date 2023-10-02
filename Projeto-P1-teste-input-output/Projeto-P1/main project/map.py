import pygame
from level import Level
from pygame.locals import *
from collectibles import *
from colors import *
from player import Player

pygame.init()
player = Player(307, 298)

class Map():
    def __init__(self, screen):
        self.all_collectibles_rects = list()  # todos os coletáveis
        self.collectibles = list()  # todos os coletáveis
        self.screen = screen
        self.walls_rects = list()  # vai estar armazenado todos os retângulos das paredes
        horizontal_walls = pygame.image.load('sprites/horizontal_woods.png')
        vertical_walls = pygame.image.load('sprites/vertical_woods.png')

        # escolha a quantidade de cada coletável:
        self.symbols_collectibles = {"r": 1, "g": 5, "b": 3, "y": 2}

        # variáveis para controlar a vitória
        self.total_objects = sum(self.symbols_collectibles.values())  # número total de objetos a serem coletados
        self.objects_collected = 0  # número de objetos já coletados
        self.reached_exit = False  # variável para controlar se o jogador alcançou a saída

        # é no eixo das abscissas e ordenadas onde o mapa está localizado
        self.x = 5
        self.y = 0
        # último valor de x e y  que foi atribuído
        self.last_x = 0
        self.last_y = 0
        self.size_map = 15  # tamanho do mapa
        self.colle_adresses = list()

        # me prevenindo caso você tenha escolhido uma quantidade muito grande
        total_collectibles = 0

        for number in self.symbols_collectibles.values():
            total_collectibles += number

        if total_collectibles >= 255:
            self.works = False
            # nesse caso o loop principal da main nem executa
            return
        else:
            self.works = True

        # esse dicionário que vai mostrar quanto foi coletado de cada um:
        self.collected = {"r": 0, "g": 0, "b": 0, "y": 0}

        level = Level()
        self.matriz_game = level.do_matriz_map()  # vai pegar a matriz do mapa
        self.draw_map(self.screen, self.x, self.y, True)  # vai desenhar o mapa

        for symbol in self.symbols_collectibles.keys():
            for _ in range(self.symbols_collectibles[symbol]):  # quantos desse tipo eu quero

                search_adress = True

                while search_adress:
                    collectible = Collectible(symbol)

                    if collectible.adress not in self.colle_adresses:  # se o endereço não foi usado
                        search_adress = False

                self.collectibles.append(collectible)
                self.matriz_game[collectible.row][collectible.column] += symbol

    def draw_map(self, screen, x, y, born):
        square_size = 60  # tamanho do quadrado
        height_square_size = 4  # tamanho do quadrado

        for row in range(self.size_map):
            for column in range(self.size_map):
                items = list(self.matriz_game[row][column])  # vai ser os símbolos de um elemento da matriz, por exemplo <^Sy

                for item in items:
                    # indicar em qual coordenada o item vai ficar, é a partir do tamanho do quadrado e onde o item está localizado na matriz e um valor dinâmico x ou y, isso faz com que o mapa movimente a partir das teclas pressionadas
                    item_x = square_size * column + x
                    item_y = square_size * row + y

                    # desenhando as paredes
                    if item in ("<", "^", ">", "v"):
                        if item == ">":
                            item_x += 60
                        elif item == "v":
                            item_y += 60

                        if item == "<" or item == ">":
                            rect = pygame.Rect(item_x, item_y, height_square_size, square_size)
                        elif item == "^" or item == "v":
                            rect = pygame.Rect(item_x, item_y, square_size, height_square_size)

                        self.walls_rects.append(rect)
                        pygame.draw.rect(screen, (255, 255, 255), rect)

                    if item in self.symbols_collectibles.keys():
                        item_x += 22
                        item_y += 22
                        size = 20

                        for collectible in self.collectibles:
                            if collectible.row == row and collectible.column == column:
                                collectible.rect = pygame.Rect(item_x, item_y, size, size)
                                pygame.draw.rect(screen, collectible.color, collectible.rect)

                    if item == "S" and born:
                        self.x = - square_size * (column) + square_size * 4
                        self.y = - square_size * (row / 2 + 2) - square_size / 2

    def move_map(self):
        self.last_x = self.x
        self.last_y = self.y

        self.pace = 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[K_w] or keys[K_s]:
            if keys[K_w]:
                self.y = self.y + self.pace

            if keys[K_s]:
                self.y = self.y - self.pace

        if keys[K_a] or keys[K_d]:
            if keys[K_a]:
                self.x = self.x + self.pace

            if keys[K_d]:
                self.x = self.x - self.pace

    def analyze_collision(self, player):

        for wall in self.walls_rects:
            if player.rect.colliderect(wall):
                self.x = self.last_x
                self.y = self.last_y
                self.pace = 0
                self.walls_rects = list()
        for collectible in self.collectibles:
            if collectible.rect.colliderect(player) and not collectible.collected:
                self.collectibles.remove(collectible)
                self.matriz_game[collectible.row][collectible.column] = self.matriz_game[collectible.row][
                                                                         collectible.column][:-1]
                self.collected[collectible.item] += 1
                collectible.collected = True
                print(self.collected)
        # verificar se o jogador coletou todos os objetos e alcançou a saída
        if self.is_exit(player.rect.center) and self.objects_collected == self.total_objects:
            self.reached_exit = True

    def is_exit(self, position):
        level = Level()
        exit_coordinates = level.find_exit_coordinates()
        exit_positions = exit_coordinates["S"] + exit_coordinates["E"]  # coordenadas de saída

        for exit_position in exit_positions:
            # verificar se a posição do jogador está próxima o suficiente de uma das saídas
            if abs(position[0] - exit_position[0]) < 30 and abs(position[1] - exit_position[1]) < 30: # coloquei 30 para verificar a proximidade mas pode ser ajustado
                return True

        return False

    def update(self, player):
        self.analyze_collision(player)
        self.move_map()
        self.draw_map(self.screen, self.x, self.y, False)

# TO-do:
# Fazer uma missão para passar de level
