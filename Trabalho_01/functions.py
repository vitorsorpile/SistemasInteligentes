import pygame

def read_txt(fileName: str):
   matrix = [[]]
   matrix.append([])
   # insert top barrier
   for _ in range(12):
      matrix[0].append(0)
   i = 1
   try:
      with open(fileName, 'r') as file:
         for line in file:
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

            i += 1
      # insert bottom barrier
      for _ in range(12):
         matrix[i].append(0)

      # print(matrix)
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