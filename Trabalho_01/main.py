import argparse
from BFS import BFS
from DFS import DFS
from functions import read_txt

parser = argparse.ArgumentParser()
parser.add_argument('-file', type=str)

args = parser.parse_args()

fileName = args.file

if fileName == None:
   fileName = 'labirintos/lab00.txt'

matrix = read_txt(fileName)


maze_solver = BFS(matrix)
maze_solver.solve()

maze_solver = DFS(matrix)
maze_solver.solve(maze_solver.root)

# raiz -> checa se é a saida
# ve os possiveis passos
# busca em profundidade -> acessa um, checa, ve os possiveis passos, acessa um ... 
# busca em largura -> acessa todos, checa um