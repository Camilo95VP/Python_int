#Condicionales simples
"""== igual que True False
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
!= diferente"""
#______________________________________________________________________________________________________________________________________________

#Programa que reciba un número e imprime si es par
numero = int(input("Digite el número: "))
if numero % 2 == 0:
    print("El número es par")
#______________________________________________________________________________________________________________________________________________

#Programa que reciba un número, imprima si es par o si es múltiplo de 3
numero = int(input("Digite el número: "))
if numero % 2 == 0:
    print(f'El número {numero} es par')
if numero % 3 == 0:
    print("El número es múltiplo de 3")
#______________________________________________________________________________________________________________________________________________

#Programa que reciba un número e imprime si ese número es par o si es impar
numero = int(input("Digite el número: "))
if numero % 2 != 0:
    print("El número es impar")
else:
    print("El número es par")
#______________________________________________________________________________________________________________________________________________

#Condiciones compuestas
""" and -> Y        true true = true
                    true false = false
                    false true = false
                    false false = false
    or -> O         true true = true
                    true false = true
                    false true= true
                    false false = false
    not ->          true = false
                    false = true"""
#______________________________________________________________________________________________________________________________________________

#Programa que reciba un número, imprima si es par y si es múltiplo de 3
numero = int(input("Digite el número: "))  #5
if numero % 2 == 0 and numero % 3 == 0:
    print("El número es par y también es múltiplo de 3")
else:
    print("El número no cumple la condición")
#______________________________________________________________________________________________________________________________________________

#Programa que reciba un número, imprima si es par o si es múltiplo de 3
numero = int(input("Digite el número: "))
if numero % 2 == 0 or numero % 3 == 0 :
    print(f'El número es par {numero%2==0} y el número es múltiplo de 3 {numero%3==0}')
else:
    print("El número no es par")
if numero % 3 == 0:
    print("El número es múltiplo de 3")
else:
    print("El número no es múltiplo de 3")
#______________________________________________________________________________________________________________________________________________

"""Realizar un programa que pida dos números enteros y muestre en pantalla el siguiente menú
CALCULADORA
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. SALIR
SELECCIONE UNA OPCION
El usuario debe digitar un número y el programa realiza el cálculo respectivo y muestra el resultado
en pantalla"""

#opcion 1
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
if opcion == 1:
    print("La suma es: ", numero1 + numero2)
if opcion == 2:
    print("La resta es: ", numero1 - numero2)
if opcion == 3:
    print("La multiplicación es: ", numero1 * numero2)
if opcion == 4:
    print("La división es: ", numero1 / numero2)
if opcion == 5:
    print("Hasta la vista")

#opcion 2 -> Condicionales anidados
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
if opcion == 1:
    print("La suma es: ", numero1 + numero2)
else:
    if opcion == 2:
        print("La resta es: ", numero1 - numero2)
    else:
        if opcion == 3:
            print("La multiplicación es: ", numero1 * numero2)
        else:
            if opcion == 4:
                print("La división es: ", numero1 / numero2)
            else:
                if opcion == 5:
                    print("Hasta la vista")
                else:
                    print("Opción invalida")

#opcion 3 elif
band = True
#ciclo inicio
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
if opcion == 1:
    print("La suma es: ", numero1 + numero2)
elif opcion == 2:
    print("La resta es: ", numero1 - numero2)
elif opcion == 3:
    print("La multiplicación es: ", numero1 * numero2)
elif opcion == 4:
    print("La división es: ", numero1 / numero2)
elif opcion == 5:
    print("Hasta la vista")
    band = False
else:
    print("Opción invalida")

#______________________________________________________________________________________________________________________________________________

"""La empresa de aviación “El pájaro loco” presta servicios entre cinco ciudades, las
cuales tiene codificadas así:
1. Medellín
2. Bogotá
3. Cali
4. Barranquilla
5. Miami
El costo de los tiquetes está definido según sea la ciudad origen, la ciudad destino y la edad del
pasajero:
• Medellín a Bogotá: 200.000 pesos más 10.000 pesos si el pasajero es menor de 60 años.
• Medellín a Cali: 250.000 pesos menos el 10% de la edad del pasajero por 1000.
• Medellín a Barranquilla: 300.000 pesos más la edad del pasajero por 1000.
• Bogotá a Medellín: 200.000 pesos, o gratis si el pasajero es mayor de 80 años.
• Bogotá a Cali: 200.000 pesos más 1000 pesos por cada año que sea menor de 60 años, sin
sobrepasar los 20.000 pesos.
• Bogotá a Barranquilla: 400.000 pesos más el 5% de la edad del pasajero por 10.000 si es mayor
de 60 años.
• Cali a Medellín: 350.000 pesos.
• Cali a Bogotá: 280.000 pesos más 20.000 pesos si el pasajero es menor de 60 años.
• Cali a Barranquilla: 190.000 pesos más 10.000 pesos si el pasajero es menor de 60 años.
• Barranquilla a Cali: 350.000 pesos más 10.000 pesos por cada año que sea mayor de 60 años.
• Barranquilla a Bogotá: 210.000 pesos más 30.000 pesos si el pasajero es menor de 30 años.
• Barranquilla a Medellín: 500.000 pesos o 250.000 si la edad del pasajero es inferior a 10 años.
• Cualquier vuelo que tenga Miami como origen o destino tiene un costo de 980.000 pesos.
Elabore un programa de computador que determine el costo del tiquete conociendo los códigos de la
ciudad origen, el destino y la edad del pasajero. """

nombre = input("Ingrese su nombre: ")
origen = input(f'{nombre} Ingrese ciudad origen: ')
destino = input(f'{nombre} ¿a donde desea viajar?: ')
edad = int(input(f'{nombre} ¿Cual es tu edad?: '))

if origen == "miami" or destino == "miami":
    costoTiquete = 980000
else:
    if origen == "medellin": 
        if destino == "bogota":
            costoTiquete = 200000
            if edad < 60:
                costoTiquete = costoTiquete + 10000
        elif destino == "cali":
            costoTiquete = 250000 - (edad * 0.1) * 1000
        elif destino == "barranquilla":
            costoTiquete = 300000 + edad * 1000
    if origen == "bogota":
        if destino == "medellin":
            if edad > 80:
                costoTiquete = "Su Tiquete es GRATIS!!"
            else:
                costoTiquete = 200000
        elif destino == "cali":
            costoTiquete = 200000
            if edad < 60:
                diferencia = 60 - edad
                if diferencia < 20:
                    sobreCosto = 20000
                else:
                    sobreCosto = diferencia * 1000
                    costoTiquete = 200000 + sobreCosto
        elif destino == "barranquilla":
            costoTiquete = 400000
            if edad > 60:
                costoTiquete = 400000 + .05 * edad * 10000
    if origen == "cali":
      if destino == "medellin":
        costoTiquete = 350000
      elif destino == "bogota":
        if edad < 60:
          costoTiquete = 280000 + 20000
        else:
          costoTiquete = 280000
      elif destino == "barranquilla":
        if edad < 60:
          costoTiquete = 190000 + 10000
        else:
          costoTiquete = 190000
    if origen == "barranquilla":  
      if destino == "cali":
            costoTiquete = 350000
            if edad > 60:
                diferencia = 60 - edad
                sobreCosto = diferencia * 10000
                costoTiquete = 350000 + sobreCosto
      elif destino == "bogota":
        costoTiquete = 210000
        if edad < 30:
          costoTiquete = costoTiquete + 30000
      elif destino == "medellin":
        costoTiquete = 500000
        if edad < 10:
          costoTiquete = 250000            
print(f'{nombre} el costo de su tiquete es: {costoTiquete}')

