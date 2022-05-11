from MazeSolver import MazeSolver
from Tree import Node


class BFS(MazeSolver):
   def __init__(self, maze):
      super().__init__(maze)

      self.list = [Node(2, None, 1, 1)]

   def solve(self):
      i = 0
      while(not self.isExit(self.list[i])):
         self.actualPos = (self.list[i].x, self.list[i].y)
         # print(self.list[i])

         steps = self.calculatePossibleSteps(self.list[i])

         if steps:
            for step in steps:
               self.list.append(step)
         i += 1
   
      # print(self.list[i])