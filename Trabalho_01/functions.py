def read_txt(fileName: str):
   matrix = [[]]
   i = 0
   try:
      with open(fileName, 'r') as file:
         for line in file:
            matrix.append([])
            line = line.strip('\n')
            line = line.replace(' ', '')
            print(line)
            for number in line:
               matrix[i].append(int(number))
            i += 1

      return matrix
      

   except Exception as e:
      print(e)