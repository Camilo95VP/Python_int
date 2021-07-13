#ciclos

#______________________________________________________________________________________________________________________________________________

#Realizar un programa que imprima los 5 primeros numeros naturales
print("1, 2, 3, 4, 5")

#______________________________________________________________________________________________________________________________________________

#Programa que imprima los 10 primeros números naturales
print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

#______________________________________________________________________________________________________________________________________________

#Programa que imprima los 100 primeros números naturales
contador = 1  
while contador <= 100:  #i, j, k
    print(contador)
    contador += 1 #contador = contador + 1

#______________________________________________________________________________________________________________________________________________

#Programa que calcule el promedio de los primeros 100 números naturales
contador = 1        #contador
suma = 0            #acumulador
while contador <= 100:
    suma = suma + contador
    contador = contador + 1
promedio = suma / (contador - 1)
print("El promedio es igual a: ", promedio)

#______________________________________________________________________________________________________________________________________________

#Programa que solicite un número al usuario y se calcule el promedio desde el 1 hasta ese número dado
limite = int(input("Digite un número"))
suma = 0
i = 1
while i <= limite:
    suma = suma + i
    i = i + 1
promedio = suma / limite
print("El promedio es igual a : ", promedio)

#______________________________________________________________________________________________________________________________________________

#Realizar un programa que imprima los números pares que hay del 1 al 100
#opcion 1
import time
start_time = time.time()
contador = 1
while contador <= 10000:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1

print("--- %s seconds ---" % (time.time() - start_time))

#opcion2
import time
start_time = time.time()
contador = 2
while contador <= 10000:
    print(contador)
    contador = contador + 2
time = (time.time() - start_time)
print("--- %s seconds ---" % time)

#______________________________________________________________________________________________________________________________________________

#Programa que imprima los 100 primeros números naturales
contador = 1
while contador <= 100:  #i, j, k
    print(contador)
    contador += 1 #contador = contador + 1

#______________________________________________________________________________________________________________________________________________

#for
#for i in range(valorInicial, valorFinal, variación):
#instrucciones del ciclo

dato = int(input("Digite el valor máximo"))
for contador in range(4,dato+1,4):         # for (contador = 1; contrador <= 100; contador=contador+1)
    print(contador)                   #    print(contador)

#______________________________________________________________________________________________________________________________________________

#hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay
nombre = input("Digite el nombre del producto: ")
cantidad = int(input("Digite la cantidad disponible del producto: "))
print(f'Del producto {nombre} se tienen {cantidad} unidades')   #Almacena un solo producto

#solicitar varios productos el nombre y la cantidad
#opcion 1
rango = int(input("Digite la cantidad de productos"))
for i in range(rango):
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))
    print(f'Del producto {nombre} se tienen {cantidad} unidades')

#opcion 2
while True:
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))
    print(f'Del producto {nombre} se tienen {cantidad} unidades')
    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '2':
        break

#______________________________________________________________________________________________________________________________________________

#Estructuras de datos  ( ) , [ ] , { }
#listas [ ] corchetes
listado = [2, 3, 4, 5, 6, 3 , 4]
print(listado)
print(listado[3])
print(len(listado)) #length tamaño

#Si quiero sumar los valores de esta lista
#opcion 1
suma = 0 #acumulador
i = 0 #contador de posicion no de valor
while i < len(listado):
    suma = suma + listado[i]
    i = i + 1

#opcion2
listado = [2, 3, 4, 5, 6, 3, 4]
suma = 0
for item in listado:
    suma = suma + item
print(suma)

listado = [2, 3, 4, 5, 6, 3, 4]
print(listado)
listado.append(6)
print(listado)
listado.remove(6)
print(listado)
print(dir(listado))

#tupla () parentesis  -> inmutable no puede cambiar  mutable o inmutable
datos = (2,3,4,5)
print(datos)
datos = (1,2,3,4)
print(datos)

#Sets { } llaves -> Conjuntos
datos = {6, 4, 2, 1}
print(datos)
#print(datos[1])   #error no hay posiciones especificas
datos.add(8)
print(datos)
datos.remove(4)
print(datos)
datos.add(8)
print(datos)

if 2 in datos:
    print("El numero 2 si se encuentra en el conjunto")

datos = {6, 4, 2, 1}
datos2 = {5, 1, 3}
print(datos)
print(datos2)
comunes = datos.intersection(datos2)
print(comunes)
todos = datos.union(datos2)
print(todos)

#______________________________________________________________________________________________________________________________________________

#Diccionarios -> Es un par llave y valor
datos = {
    'nombre': 'Edwin',
    'apellido': 'Cubillos',
    'cedula': '12345678',
    'edad': 38
}
print(datos)

producto = {
    'nombre': 'fab',
    'cantidad': 2
}

#Agregar elementos al dicccionario
datos = {
    'nombre': 'Edwin',
    'apellido': 'Cubillos',
    'cedula': '12345678',
    'edad': 38
}
print(datos)
datos['correo'] = "edwin@gmail.com"
print(datos)

#imprimir un diccionario
for i in datos:  #imprime la llave
    print(i)

for i in datos.values():   #imprime el valor
    print(i)

for llave, valor in datos.items():  #imprime el par de llave y valor
    print(llave, " \t ", valor)

#______________________________________________________________________________________________________________________________________________

#hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay
inventario = []
nombre: input("ingrese nombre del producto: ")         #creamos una lista vacía
while nombre != "":             #ciclo infinito
    cantidad = int(input("Digite la cantidad disponible del producto: "))

    producto = {           #creo mi diccionario
        'nombre': nombre,
        'cantidad': cantidad
    }

    inventario.append(producto)
    
    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '1':  #condicion finalizar el ciclo
         nombre = input("Ingrese nombre del producto: ")
    elif continuar == '2':
        print("Hasta pronto ...")
    

for i in inventario:
    print("Del producto", i['nombre'], "usted tienen ",i['cantidad'], "unidades")

#______________________________________________________________________________________________________________________________________________

#hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay
#version2

inventario = [] #creamos una lista vacía
nombre = input("ingrese nombre del producto: ")         
while nombre != "": 
    cantidad = int(input("Digite la cantidad disponible del producto: "))

    producto = {           #creo mi diccionario
        'nombre': nombre,
        'cantidad': cantidad
    }

    inventario.append(producto)
    
    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '1':  #condicion 
     nombre = input("Ingrese nombre del producto: ")
     continue #instruccion para repetir el ciclo
    elif continuar == '2':
      break  #instriccion para parar el ciclo y pasara la linea o bloque de abajo

for i in inventario:
    print("Del producto", i['nombre'], "usted tienen ",i['cantidad'], "unidades")
    print("Hasta pronto ...")

#______________________________________________________________________________________________________________________________________________

#Determinar el salario de empleados de una emmpresa, el aumento, y la cantidad de empleados procesados.

contador = 0
nombre = input("entre nombre ")

while nombre != "":
   salario = int(input(f"{nombre} entre salario "))
   contador = contador + 1
   aumento = 0.1
   if salario < 1000:
    aumento = salario * 0.1
   nuevoSalario = salario + aumento
   print("Nombre", nombre, "salario", salario, "Aumento", aumento, "Nuevo salario", nuevoSalario)
   nombre = input("entre nombre ")
print("Total empleados", contador)

#______________________________________________________________________________________________________________________________________________

"""
Un segundo ejercicio es calcular el factorial de un entero n. El factorial de un número entero n se define como la productoria 
de todos los enteros desde 1 hasta n. Así, el factorial de 5 es el producto de 1 * 2 * 3 * 4 * 5, lo cual da 120. 
Es un algoritmo similar al de la sumatoria, con la diferencia de que, en vez de hacer sumas sucesivas, 
lo que hacemos es multiplicaciones sucesivas."""

n = int(input("entre número entero "))

producto = 1

consecutivo = 1

while consecutivo <= n:

            producto = producto * consecutivo

            consecutivo = consecutivo + 1

print("El factorial de", n, "es", producto)

#______________________________________________________________________________________________________________________________________________

#Programa que imprima la tabla de multiplicar de un numero n desde el 1 hasta el 10 y entregue el resultado

n = int(input("entre número entero "))
i = 1
while i <= 10:
     r = n * i
     print(n, "*", i, "=", r)
     i = i + 1
print("terminé\n")

#______________________________________________________________________________________________________________________________________________
#Cilos anidados

"""Algoritmo de varias tablas de multiplicar. Elaborar un algoritmo que lea un entero n y que calcule e imprima todas las tablas de multiplicar 
desde 1 hasta n, cada tabla desde 1 hasta 10.

En este caso, si el número leído es 5, debemos generar e imprimir la tabla de multiplicar del 1, desde 1 hasta 10; la tabla de multiplicar del 2, 
desde 1 hasta 10; la tabla de multiplicar del 3, desde 1 hasta 10; la tabla de multiplicar del 4, desde 1 hasta 10; la tabla de multiplicar del 5, desde 1 hasta 10.

En nuestro algoritmo anterior leíamos un número n y generábamos e imprimíamos la tabla de multiplicar de n, desde 1 hasta 10. Ahora lo que necesitamos 
es generar las n desde 1 hasta 5, y para cada valor de n escribir las instrucciones correspondientes al algoritmo anterior.

Datos de entrada: número entero n.
Cálculos: generar todos los enteros desde 1 hasta n: utilizaremos una variable x, la cual variará desde 1 hasta n, y por cada valor de x generamos 
e imprimimos la tabla de multiplicar desde 1 hasta 10.
Datos de salida: tablas de multiplicar desde 1 hasta n, cada tabla desde 1 hasta 10.
Nuestro programa es:"""

n = int(input("entre número entero "))

x = 1

while x <= n:

            i = 1

            while i <= 10:

                        r = x * i

                        print(x, "*", i, "=", r)

                        i = i + 1

            x = x + 1

            print(" ")


