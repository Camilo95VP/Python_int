# Juego en el cual tienes que adivinar numeros y su posicion

# primer paso seleccion de dificultad puede ser 3 numeros 4 o 5 (facil medio dificil)


print("Bienvenido al juego numerico")
print("La idea del juego es adivinar la combinacion de numeros enteros(0-9) en la menor cantidad de intentos,\nNo hay numeros repetidos en las combinaciones.")
difficulty = int(input("Seleccione una dificultad: \n1)Facil \n2)Medio \n3)Dificil \n: "))

import random

if difficulty == 1:
    cantidad_digitos = 3

elif difficulty == 2:
    cantidad_digitos = 4

elif difficulty == 3:
    cantidad_digitos = 5

list_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
solution = []

for i in range(0, cantidad_digitos):
    agregar = (random.choice(list_digits))

    while agregar in solution:
        agregar = (random.choice(list_digits))

    solution.append(agregar)

option = []
contador_intentos = 0

while option != solution:
    contador_intentos += 1
    position = 0
    option = []
    correct_number = 0
    correct_position = 0

    print(f"Por favor ingrese una combinacion de {cantidad_digitos} numeros enteros (0-9) ")

    for j in range(0, cantidad_digitos):

        selection_numbers = int(input(f"\n Ingrese el numero de la posicion {position+1}: "))
        option.append(selection_numbers)

        for k in range(0,1):
            if option[position] == solution[position]:
                correct_position += 1
            if option[position] in solution:
                correct_number += 1

        position += 1

    print(f"Tiene {correct_number} numeros correctos y {correct_position} bien ubicados.")


print(f"La solucion {option} es correcta lo logro en {contador_intentos} intentos.")
