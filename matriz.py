#Creacion de una matriz

import random
m = int(input("\nEntre número de filas de la matriz: "))
n = int(input("\nEntre número de columnas de la matriz: "))
mat = [] * (m+1)
for i in range(m+1):
    a = [0]*(n+1)
    mat.append(a)
for i in range(1, m + 1):
  for j in range(1, n + 1):
    mat[i][j] = random.randint(0, 9)
    print(mat[i][j], end = ', ')
  print()
print()  

for i in range(1, m + 1):
  s = 0
  for j in range(1, n + 1):
    s = s + mat[i][j]
  print(f'El total de la fila {i} es:',s)
