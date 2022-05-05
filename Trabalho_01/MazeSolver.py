from Tree import Tree, Node

START_VALUE = 2
EXIT_VALUE = 3
PROFUNDIDADE = 1

class MazeSolver():
   def __init__(self, maze):
      self.tree = Tree()
      self.maze = maze
      self.actualPos = (1,1)
      self.root = Node(2, None, 1, 1)

   def calculatePossibleSteps(self, node):
      if node == None:
         return
      
      if node.root != None:
         aux = self.maze[node.root.x][node.root.y]
         self.maze[node.root.x][node.root.y] = 0

      value = self.maze[node.x + 1][node.y]
      if value != 0:
         node.addLeaf(value, node.x + 1, node.y)

      value = self.maze[node.x - 1][node.y]
      if value != 0:
         node.addLeaf(value, node.x - 1, node.y)

      value = self.maze[node.x][node.y + 1]
      if value != 0:
         node.addLeaf(value, node.x, node.y + 1)

      value = self.maze[node.x][node.y - 1]
      if value != 0:
         node.addLeaf(value, node.x, node.y - 1)

      if node.root != None:
         self.maze[node.root.x][node.root.y] = aux

      


   def isExit(self, node):
      if node.value == EXIT_VALUE:
         return True 
      else:
         return False

   
   def solve(self, searchAlgorithm, node):
      if node == None:
         return

      print(node)
      if self.isExit(node):
         return True

      self.calculatePossibleSteps(node)
      #for leaf in node.leaves:
      #   print(leaf, end=', ')

      #print('')

      for leaf in node.leaves:
         if searchAlgorithm == PROFUNDIDADE:
            ret = self.solve(searchAlgorithm, leaf)
            if (ret == None):
               continue
            return ret

      
            