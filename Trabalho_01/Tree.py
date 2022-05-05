
from re import X

from matplotlib.pyplot import xscale
from sympy import false


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
      return f'({self.x}, {self.y}) -> {self.value}'
   
   def addLeaf(self, value, x, y):
      self.leaves.append(Node(value, self, x, y))


  # def computeLeaves(self):
  #    value = self.matrix[self.x + 1][self.y]
   #   if value != 0:
    #     self.addLeaf(value, self.x + 1, self.y)
#
 #     value = self.matrix[self.x - 1][self.y]
  #    if value != 0:
   #      self.addLeaf(value, self.x - 1, self.y)
#
 #     value = self.matrix[self.x][self.y + 1]
  #    if value != 0:
   #      self.addLeaf(value, self.x, self.y + 1)
#
 #     value = self.matrix[self.x][self.y - 1]
  #    if value != 0:
   #      self.addLeaf(value, self.x, self.y - 1)

      
class Tree():
   def __init__(self):
      self.root = None

   def insertNode(self):
      newNode = Node()