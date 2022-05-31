from time import sleep
from MazeSolver import MazeSolver
from Tree import Node
import pygame

from functions import visualizeMatrix

class BFS(MazeSolver):
   def __init__(self, maze, screen):
      super().__init__(maze,screen)
      self.list = [Node(2, None, 1, 1)]

   def solve(self):
      i = 0
      while(not self.isExit(self.list[i])):
         self.updateActualPos(self.list[i].x, self.list[i].y)
         print(self.list[i])
         steps = self.calculatePossibleSteps(self.list[i])
         #print(steps)
         visualizeMatrix(self.maze,self.screen)
         pygame.display.update()
         sleep(0.5)
         if steps:
            for step in steps:
               self.list.append(step)
         i += 1

      self.updateActualPos(self.list[i].x, self.list[i].y)
      visualizeMatrix(self.maze,self.screen)
      pygame.display.update()
      sleep(0.5)
      print(self.list[i])
      print(f'BFS solved the maze in {i} steps.')