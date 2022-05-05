from MazeSolver import MazeSolver

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-file', type=str)

args = parser.parse_args()

fileName = args.file

if fileName == None:
   fileName = 'labirintos/lab00.txt'

matrix = [[]]
i = 0
try:
   with open(fileName, 'r') as file:
      for line in file:
         matrix.append([])
         line = line.strip('\n')
         line = line.replace(' ', '')
         print(line)
         for number in line:
            matrix[i].append(int(number))
         i += 1

   print(matrix)

except Exception as e:
   print(e)


maze_solver = MazeSolver(matrix)
maze_solver.solve(1, maze_solver.root)

# raiz -> checa se é a saida
# ve os possiveis passos
# busca em profundidade -> acessa um, checa, ve os possiveis passos, acessa um ... 
# busca em largura -> acessa todos, checa um