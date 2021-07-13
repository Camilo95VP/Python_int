A = [[2,6,8], 
     [2,1,7], 
     [9,8,3]]

valor_minimo = A[0][1]
posFila = 0
porColumna = 0

n = len(A)
for fila in range (n):
  for columna in range (n):
    if(fila+columna)%2 != 0 and (fila+columna) <= n - 1:
     if A[fila][columna] <= valor_minimo:
      valor_minimo = A[fila][columna]
      
lista_posiciones = []  

for fila in range (n):
  for columna in range (n):
    if A[fila][columna] == valor_minimo and (fila+columna) <= n - 1 and (fila+columna)%2 != 0:
      posFila = fila
      posColumna = columna
      lista_posiciones.append((posFila,posColumna))

posiciones_valor_minimo = tuple(lista_posiciones)
      
print("El dato menor es:", valor_minimo)
print(f'Y esta en la posicion {posiciones_valor_minimo}')