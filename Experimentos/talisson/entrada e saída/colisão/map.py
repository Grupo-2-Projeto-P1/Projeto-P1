# dentro da class map e antes da função draw_map

  def find_exit_position(self):
       for row in range(self.size_map):
         for column in range(self.size_map):
           if 'S' in self.matriz_game[row][column]:
             return (row, column)
       return None

