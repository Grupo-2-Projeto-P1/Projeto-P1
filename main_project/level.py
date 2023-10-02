import cv2

class Level:
  def __init__(self):
    self.size = 15 # Tamanho da matriz  
    maze_number = 1
    self.level_photo = cv2.imread(f"./assets/levels/0/maze{maze_number}.png") # Pega uma estrutura de mapa aleatorio a partir do nivel
    self.matriz = list()

  def do_matriz_map(self):
    for column in range(self.size):
      elements_row = list() # Representa uma linha da matriz
      for row in range(self.size):
        # Separamos a imagem do labirinto em quadrados 16x16, porém, todo o contorno da imagem tem uma grossura de 2 pixels, mas
        # queremos contablizar a partir do pixel 2, por isso, o mais 1 dessa conta a baixo
        slice_photo = self.level_photo[(column * 16) + 1 : ((column + 1) * 16 + 1), (row * 16) + 1 : ((row + 1) * 16) + 1] # Pega um quadrado do labirindo 16x16
        string = str() # vai ser os simbolos de cada quadrado, por exemplo: "<^Sy", tem parede em cima e do lado esquerdo, é onde o player vai nascer e tem um coletavel

        # Esses simbolos a baixo vai servir para mostrar ao código onde tem parede, ou seja, 
        # < - Parede no lado esquerdo
        # ^ - Parede em cima
        # > - Parede no lado direito
        # v - Parede embaixo

        # Aqui estamos pegando 4 pontos: esquerdo-centro, cima-centro, direito-centro, baixo-centro
        left_point = tuple(slice_photo[8,0])
        up_point = tuple(slice_photo[0,8])
        right_point = tuple(slice_photo[8,15])
        down_point = tuple(slice_photo[15,8])
        all_points = [left_point, up_point, right_point, down_point] 

        # Se um desses pontos forem preto, isso quer dizer que tem uma parede ali
        if (0,0,0) == left_point: string += "<"
        if (0,0,0) == up_point: string += "^"
        if (0,0,0) == right_point: string += ">"
        if (0,0,0) == down_point: string += "v"

        # Verifica o começo e o fim do labirinto, se a cor for vermelha, então, ele irá colocar um E na string, caso seja verda, será S
        for point in all_points:
          if point == (0,0,255):
            string += "E"
          if point == (0,255,0):
            string += "S"

        elements_row.append(string)

      self.matriz.append(elements_row)
    return self.matriz

# level = Level()
# level.do_matriz_map()
