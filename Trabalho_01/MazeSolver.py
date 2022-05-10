import random
from Tree import Tree, Node
import copy

START_VALUE = 2
EXIT_VALUE = 3
DFS = 1
BFS = 2

class MazeSolver():
   def __init__(self, maze):
      self.maze = maze
      self.actualPos = (1,1)

      self.root = Node(2, None, 1, 1)
      self.tree = Tree(self.root)
      
   def calculatePossibleSteps(self, node):
      if node == None:
         return
      
      if node.root != None:
         aux = self.maze[node.root.x][node.root.y]
         self.maze[node.root.x][node.root.y] = 0

      possibleSteps = []

      value = self.maze[node.x + 1][node.y]
      if value != 0:
         possibleSteps.append(Node(value, None, node.x + 1, node.y))
         # node.addLeaf(value, node.x + 1, node.y)

      value = self.maze[node.x - 1][node.y]
      if value != 0:
         possibleSteps.append(Node(value, None, node.x - 1, node.y))
         # node.addLeaf(value, node.x - 1, node.y)

      value = self.maze[node.x][node.y + 1]
      if value != 0:
         possibleSteps.append(Node(value, None, node.x, node.y + 1))
         # node.addLeaf(value, node.x, node.y + 1)

      value = self.maze[node.x][node.y - 1]
      if value != 0:
         possibleSteps.append(Node(value, None, node.x, node.y - 1))
         # node.addLeaf(value, node.x, node.y - 1)

      if node.root != None:
         self.maze[node.root.x][node.root.y] = aux

      return possibleSteps


   def isExit(self, node):
      if node.value == EXIT_VALUE:
         return True 
      else:
         return False

   
   def solve(self, node):
      if node == None:
         return

      print(node)
      self.actualPos = (node.x, node.y)

      print(self.actualPos)
      
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

