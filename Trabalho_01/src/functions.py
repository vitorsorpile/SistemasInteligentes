import pygame

def read_txt(fileName: str):
   matrix = [[]]
   # insert top barrier
   n = 0
   i = 0
   try:
      with open(fileName, 'r') as file:
         
         for line in file:
            print(line)
            matrix.append([])
            # insert left side barrier
            matrix[i].append(0)

            line = line.strip('\n')
            line = line.replace(' ', '')
            #print(line)
            for number in line:
               matrix[i].append(int(number))

            # insert right side barrier 
            matrix[i].append(0)

            #print(matrix[i])
            i += 1
      n = len(matrix[0])
      #insert top and bottom barrier
      matrix.insert(0, [])

      for _ in range(n):
         matrix[0].append(0)
         matrix[n-1].append(0)

      print('------------------')
      for line in matrix:
         print(line)
      print('-------------------')
      return matrix
      

   except Exception as e:
      print(e)

def createSquare(x,y,color,gridDisplay):
   pygame.draw.rect(gridDisplay,color,[x,y,35,35])

def visualizeMatrix(mazematrix,gridDisplay):
   y = 0
   for row in mazematrix:
      x = 0
      for item in row:
         if item == 0:
            createSquare(x,y,(255,255,255),gridDisplay)
         if item == 1 or item == 2:
            createSquare(x,y,(0,0,0),gridDisplay)
         if item == 3:
            createSquare(x,y,(255,0,0),gridDisplay)
         if item == 4:
            createSquare(x,y,(0,255,0),gridDisplay)
         x += 35
      y += 35