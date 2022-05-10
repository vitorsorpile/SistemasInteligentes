
class Node():
   def __init__(self, value, root, x, y):
      self.leaves = []
      self.value = value
      self.root = root
      self.x = x
      self.y = y
      # self.matrix = matrix
   
   def __eq__(self, o):
      if o == None:
         return False

      if self.x == o.x and self.y == o.y:
         return True

      return False

   def __str__(self):
      # Logica de x e y na matriz eh invertida com o plano cartesiano
      return f'({self.y}, {self.x}) -> {self.value}'
   
   def addLeaf(self, value, x, y):
      self.leaves.append(Node(value, self, x, y))

   def printTree(self, level = 0):
      ret = ' '*2*level + str(self) + '\n'
      for leaf in self.leaves:
         ret += leaf.printTree(level + 1)
      return ret

      
class Tree():
   def __init__(self, root = None):
      self.root = root

   def __str__(self):
     return  self.root.printTree()
      