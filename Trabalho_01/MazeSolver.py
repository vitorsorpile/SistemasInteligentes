from Tree import Node

START_VALUE = 2
EXIT_VALUE = 3
DFS = 1
BFS = 2

class MazeSolver():
   def __init__(self, maze):
      self.maze = maze
      self.actualPos = (1,1)
      
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
         print(f'Exit is at ({node.x},{node.y})')
         return True 
      else:
         return False

   
   def solve(self, node):
      raise NotImplementedError()

