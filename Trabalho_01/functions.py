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