from MazeSolver import MazeSolver
from Tree import Node, Tree
import random


class DFS(MazeSolver):
   def __init__(self, maze):
      super().__init__(maze)

      self.root = Node(2, None, 1, 1)
      self.tree = Tree(self.root)

   def solve(self, node):
      if node == None:
         return

      print(node)
      self.actualPos = (node.x, node.y)

      # print(self.actualPos)
      
      if self.isExit(node):
         return True

      steps = self.calculatePossibleSteps(node)
      
      for step in steps:
         step.root = node
         node.leaves.append(step)
      #for leaf in node.leaves:
      #   print(leaf, end=', ')
      
      #print('')
      #aux = copy.copy(node.leaves)
      aux = list(range(len(node.leaves)))

      random.shuffle(aux)      

      for index in aux:
         ret = self.solve(node.leaves[index])
         if (ret == None):
            continue
         return ret

#      for leaf in node.leaves:
 #        ret = self.solve(leaf)
  #       if (ret == None):
   #         continue
    #     return ret