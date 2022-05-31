import argparse
from time import sleep
from BFS import BFS
from DFS import DFS
from functions import read_txt
import pygame
from sys import exit
import tkinter as tk
from tkinter import filedialog
import interface

parser = argparse.ArgumentParser()
parser.add_argument('-file', type=str)

args = parser.parse_args()

fileName = args.file

root = tk.Tk()
root.withdraw()

pygame.init()
screen1 = pygame.display.set_mode((400,400))
pygame.display.set_caption('Maze Solver by Vitor Sorpile & Paulo Gorla')

dfs_img = pygame.image.load('figuras/botao_dfs.PNG').convert_alpha()
bfs_img = pygame.image.load('figuras/botao_bfs.PNG').convert_alpha()
select_maze_img = pygame.image.load('figuras/botao_select_maze.PNG').convert_alpha()

logo_img = pygame.image.load('figuras/logo.PNG').convert_alpha()
creditos_img = pygame.image.load('figuras/creditos.PNG').convert_alpha()
end_img = pygame.image.load('figuras/end.PNG').convert_alpha()

logo = interface.Image(115,40,logo_img,0.5,screen1)
creditos =interface.Image(235,385,creditos_img,0.5,screen1)
end = interface.Image(70,170,end_img,0.7,screen1)

dfs_button = interface.Button(30,160,dfs_img,0.25,screen1)
bfs_button = interface.Button(208,160,bfs_img,0.25,screen1)
select_maze_button = interface.Button(37,235,select_maze_img,0.5,screen1)

while True:
   screen1.fill((255,255,255))
   logo.draw()
   creditos.draw()

   if select_maze_button.draw():
      fileName = filedialog.askopenfilename()

   if dfs_button.draw():
      if fileName == None:
         fileName = 'labirintos/lab00.txt'

      matrix = read_txt(fileName)
      maze_solver_dfs = DFS(matrix,screen1)
      maze_solver_dfs.solve(maze_solver_dfs.root)
      screen1.fill((255,255,255))
      end.draw()
      pygame.display.update()
      sleep(2)
      #pygame.quit()
      #exit()

   if bfs_button.draw():
      if fileName == None:
         fileName = 'labirintos/lab00.txt'

      matrix = read_txt(fileName)
      maze_solver_bfs = BFS(matrix, screen1)
      maze_solver_bfs.solve()
      screen1.fill((255,255,255))
      end.draw()
      pygame.display.update()
      sleep(2)
      #pygame.quit()
      #exit()
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
   pygame.display.update()
pygame.quit()
# raiz -> checa se é a saida
# ve os possiveis passos
# busca em profundidade -> acessa um, checa, ve os possiveis passos, acessa um ... 
# busca em largura -> acessa todos, checa um