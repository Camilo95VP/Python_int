import math
import datetime
#Lea desde el teclado el nombre y la edad de cualquier persona e imprima tanto el nombre como la edad

nombre = input("Escriba su nombre:")
edad = int(input("Digite su edad:"))

print(f' El nombre es: {nombre} y la edad es: {edad}')

#Lea dos números. Calcule la suma e imprima la suma y los dos números.

numero1 = int(input("numero1:"))  #Entrada de informacion
numero2 = int(input("numero2:"))

suma = numero1 + numero2    #Proceso de informacion

print(f'La suma de {numero1} mas {numero2} es igual a: {suma}') #Salida de Datos

#Leer un número y calcular el 5% del número leído.

numero = int(input("Digite numero:"))

porcentaje = int(input("Ingrese porcentaje a sacar"))

calculo = numero * porcentaje / 100

print(f'El {porcentaje} % de: {numero} es: {calculo}')

#.Elabore un programa que realice la conversión de libras a kilogramos
#Donde 1 Kg. = 2.2046 libras.

libra = int(input("Digite cantidad de Libras"))

calculo = libra * 1 / 2.2046

print(f' {libra} Libras equivalen a {calculo} Kilogramos')

# Elaborar un algoritmo que imprima Z

e = float(input("Ingrese e: "))
z = 1 / (2 * math.pi) **(1/2) * e

print(z)

#Elaborar un algoritmo que lea el radio de una esfera y calcule el volumen y el area

radio = float(input("Ingrese Radio: "))
volumen = (4*math.pi*radio**3)/3
area = math.pi*radio**2

print(f'El Volumen de la esfera es : {volumen} y el Area es: {area}')

# Dada un cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad cambiaría es un dato desconocido

pesos = int(input("Digite Pesos Colombianos: "))

calculo = int(pesos * 0.0002678) 

print(f'{pesos} Pesos son: {calculo} Dolares')

#Calcular el área de un círculo conociendo su radio

radio = int(input("Ingrese Radio"))

calculo = math.pi*radio**2

print(f'El area del circulo es: {calculo}')

#Calcular el área de un rectángulo

base = int(input("Ingrese base: "))
altura = int(input("Ingrese Altura: "))

formula = base * altura

print(f'El area es: {formula}')

#Calcule e imprima el promedio de edad de 3 personas

ededPersona1 = int(input("Edad Persona1: "))
ededPersona2 = int(input("Edad Persona2: "))
ededPersona3 = int(input("Edad Persona3: "))

promedio = int(ededPersona1 + ededPersona2 + ededPersona3) / 3
    
print(f'El Promedio de edad es: {promedio} ')

#El sueldo neto de un vendedor se calcula como la suma de un sueldo básico
#de 450.000 más el 12% del monto total vendido. Diseñe un algoritmo que
#determine el sueldo neto de un vendedor sabiendo que hizo tres ventas en el mes.

sueldoNeto = int(450000)

venta1 = int(input("Ingrese venta1: "))
venta2 = int(input("Ingrese Venta2: "))
venta3 = int(input("Ingrese venta3: "))

comision = int(venta1 + venta2 + venta3) * 0.12
print(f'Su comision es de: {comision}')

sueldoTotal = int(comision + sueldoNeto)

print(f'Su sueldo es: {sueldoTotal}$ ')

#Fecha y Hora

hoy = datetime.date.today()
print(hoy)

#Elaborar un algoritmo que lea el salario actual de un empleado y que calcule e imprima el nuevo salario con base en la siguiente condición: 
#si el salario es menor que 1000 pesos, aumente el 10%; de lo contrario, no haga aumento.

salact = float(input("entre salario actual "))
au = 0
if salact < 1000:
        au = salact * 0.1
nuesal = salact + au
print("salario actual ", salact, "aumento ", au, "nuevo salario ", nuesal) 

salact = float(input("entre salario actual "))
au = 0
if salact < 1000:
        au = salact * 0.1
nuesal = salact + au
print("salario actual ", salact, "aumento ", au, "nuevo salario ", nuesal)

#____________________________________________________________________________________________________________________________________________________

numero1 = int(input("numero1: "))
numero2 = int(input("numero2: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
modulo = numero1 % numero2  

print(f'{numero1} + {numero2} = {suma} \n{numero1} - {numero2} = {resta} \n{numero1} * {numero2} = {multiplicacion} \n{numero1} / {numero2} = {division} \n{numero1} % {numero2} = {modulo}')

#____________________________________________________________________________________________________________________________________________________


entero = int(input("Ingrese numero: "))
lista = [entero]
suma = 0
i = 0
while entero > 0:
    entero = int(input("Ingrese numero: "))

    while i < len(lista):
      if entero > 0:
        if lista[i] % 2 == 0:
            suma = suma + lista[i]
        i = i + 1
print('La suma de los numeros pares es:', suma)