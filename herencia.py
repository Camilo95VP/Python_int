#Herencia
#Clase -> Abstracción - Modelo de un objeto de la vida real
# atributos -> Cualidades -> color, modelo, marca,
# y metodos -> Funciones o acciones ->

"""class Persona:                                          #Clase Padre
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def imprimirDatos(self):
        print(f'Nombre: {self.nombre}, edad: {self.edad}, telefono {self.telefono}')

class Empleado(Persona):                                         #Clase Hijo
    def __init__(self, nombre, edad, telefono, salario, empresa):
        super().__init__(nombre, edad, telefono)
        self.salario = salario
        self.empresa = empresa

    def imprimirDatosEmpleado(self):
        print(f'Salario: {self.salario}, Empresa: {self.empresa}')

class Estudiante(Persona):                                        #Clase Hijo
    def __init__(self, nombre, edad, telefono, carrera, universidad):
        super().__init__(nombre, edad, telefono)
        self.carrera = carrera
        self.universidad = universidad

    def imprimirDatosEstudiante(self):
        print(f'Carrera: {self.carrera}, Universidad: {self.universidad}')

empleado1 = Empleado (telefono = '3146561244', salario = 5000000, edad = 28 , empresa = 'Pragma', nombre = 'James')
empleado1.imprimirDatos()
empleado1.imprimirDatosEmpleado()

estudiante1 = Estudiante (telefono = '312456789', edad = 30, nombre = 'Juan', carrera = 'Sicología', universidad = 'Luis Amigo')
estudiante1.imprimirDatos()
estudiante1.imprimirDatosEstudiante()
#______________________________________________________________________________________________________________________________________________s
#Ejemplo 2
#Ejercicio Definir una clase padre llamada vehículo y dos clases llamadas carro y bicicleta
#vehiculo - atributos: color, ruedas métodos: __init__
#coche - atributos: velocidad método: __init__
#bicicleta - atributos: tipo (urbana / montaña / ruta) __init__

class Vehiculo():
    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + " Ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

class Bicicleta(Vehiculo):
    def __init__(self,  color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

vehiculo = Vehiculo("Rojo", 4)
print (vehiculo)
print(f'color: {vehiculo.color}, ruedas: {vehiculo.ruedas}')

coche = Coche ("Azul", 4, 200)
print(f'color: {coche.color}, ruedas: {coche.ruedas}, velocidad: {coche.velocidad} km/h')

bicicleta = Bicicleta("Negra", 2, "MTB")
print(f'color: {bicicleta.color}, ruedas: {bicicleta.ruedas}, tipo: {bicicleta.tipo}')"""
#______________________________________________________________________________________________________________________________________________
#Programa completo: Inventario de un supermercado
#Producto -> atributos: nombre, precio, marca, cantidad, fechaDeVencimiento
#Lacteos -> atributos: volumen, tipo (entero, deslactosado, descremado), presentacion (caja, bolsa, vaso)
#Detergente -> atributos: tipoDeUso (cocina, baño,ropa), presentacion (liquido, polvo, barra)
#Licores -> atributos: tipo (cerveza, whisky), origen (nacional, importando), porcentajeAlcohol

class Producto(): #padre
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return "Nombre: " + self.nombre + ", Precio: " + str(self.precio) + ", Cantidad: " + str(self.cantidad)

class Lacteos(Producto): #hijo(hereda las 3 propiedades del padre)
    def __init__(self,nombre, precio, cantidad, volumen, tipo, presentacion): #contructor
        super().__init__(nombre, precio, cantidad) #llamando al padre a traves de super
        self.volumen = volumen #propiedades diferentes a las heredadas del padre
        self.tipo = tipo
        self.presentacion = presentacion
    
    def __str__(self):
        return super().__str__() + ", Volumen: " + str(self.volumen) + ", tipo: " + self.tipo + ", presentacion: " + self.presentacion    

class Detergente(Producto): #hijo(hereda las 3 propiedades del padre)
    def __init__(self, nombre, precio, cantidad, tipoDeUso, presentacion):
        super().__init__(nombre, precio, cantidad)
        self.tipoDeUso = tipoDeUso
        self.presentacion = presentacion       

    def __str__(self):
        return super().__str__() + ", Tipo de uso: " + self.tipoDeUso + ", presentacion: " + self.presentacion

class Licores(Producto): #hijo(hereda las 3 propiedades del padre)
    def __init__(self, nombre, precio, cantidad, tipoAlcohol, origen, porcentajeAlcohol):
        super().__init__(nombre, precio, cantidad)
        self.tipoAlcohol = tipoAlcohol
        self.origen = origen
        self.porcentajeAlcohol = porcentajeAlcohol

    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipoAlcohol + ", Origen: " + self.origen + ", PorcentajeAlcohol: " + self.porcentajeAlcohol

def imprimirMenu(): #crud
    opcion = int(input("1. Agregar Producto\n2. Buscar Producto\n3. Eliminar Producto\n4. Actualizar Producto\n5. Mostrar inventario\n6. Salir"))
    return opcion

lacteosList = [] #listas vacias para poder iterar sobre ellas
detergentesList = []
licoresList = []

while (True):
    opcion = imprimirMenu() #llamando crud
    
    #_______________________________AGREGAR PRODUCTO___________________________________  
    
    if opcion == 1:
        tipo = int(input("Seleccione el tipo de producto:\n1. Lacteo\n2. Detergente\n3. Licores"))
      
        if tipo == 1:  #Lacteo
            nombre = input("Digite el nombre: ")
            precio = int(input("Digite el precio: "))
            cantidad = int(input("Digite la cantidad: "))
            volumen = int(input("Digite el volumen: "))
            tipo = input("Digite el tipo: ")
            presentacion = input("Digite la presentación: ")
            lacteo = Lacteos(nombre, precio, cantidad, volumen, tipo, presentacion)
            lacteosList.append(lacteo)
        
        elif tipo == 2: #Detergente
            nombre = input("Digite el nombre: ")
            precio = int(input("Digite el precio: "))
            cantidad = int(input("Digite la cantidad: "))
            tipoDeUso = input("Digite tipo de uso: ")
            presentacion = (input(f'Digite la presentacion del {nombre}: '))
            detergente = Detergente(nombre, precio, cantidad, tipoDeUso, presentacion)
            detergentesList.append(detergente)

        elif tipo == 3: #Licor
            nombre = input("Digite el nombre: ")
            precio = int(input("Digite el precio: "))
            cantidad = int(input("Digite la cantidad: "))
            tipoAlcohol = input("Digite tipo de Alcohol: ")
            origen = input("Digite Origen: ")
            porcentajeAlcohol = int(input("Digite porcentaje de alcohol: "))
            licores = Licores(nombre, precio, cantidad, tipoAlcohol, origen, porcentajeAlcohol)
            licoresList.append(licores)

    #_______________________________BUSCAR PRODUCTO___________________________________


    elif opcion == 2:
        productoAbuscar = input("Digite el producto a buscar: ")
        existeElProducto = False
        
        for lacteo in lacteosList:
            if lacteo.nombre == productoAbuscar:
                print(f'El producto {lacteo.nombre} existe en el inventario de Lacteos')
                existeElProducto = True
        if existeElProducto == False:
            print("El producto no existe")    
        
        for detergente in detergentesList:
            if detergente.nombre == productoAbuscar:
                print(f'El producto {detergente.nombre} existe en el inventario de Detergentes')
                existeElProducto = True
        if existeElProducto == False:
            print("El producto no existe")

        for licores in licoresList:
            if licores.nombre == productoAbuscar:
                print(f'El producto {licores.nombre} existe en el inventario de Licores')
                existeElProducto = True
        if existeElProducto == False:
            print("El producto no existe")

    #_______________________________ELIMINAR PRODUCTO___________________________________


    elif opcion == 3:
        productoAbuscar = input("Digite nombre del producto que desea eliminar: ")
        existeElProducto = False
        
        for lacteo in lacteosList:
            if lacteo.nombre == productoAbuscar:
                confirmacion = input(F'Confirma que desea eliminar el producto {lacteo.nombre} s / n')
                if confirmacion == 's':
                    lacteosList.remove(lacteo)
                    print(f'El producto {lacteo.nombre} se elimino correctamente')
                existeElPeluche = True
        if existeElPeluche == False:
            print("El producto no existe")

        for detergente in detergentesList:
            if detergente.nombre == productoAbuscar:
                confirmacion = input(F'Confirma que desea eliminar el producto {detergente.nombre} s / n')
                if confirmacion == 's':
                    detergentesList.remove(detergente)
                    print(f'El producto {detergente.nombre} se elimino correctamente')
                existeElPeluche = True
        if existeElPeluche == False:
            print("El producto no existe")

        for licores in licoresList:
            if licores.nombre == productoAbuscar:
                confirmacion = input(F'Confirma que desea eliminar el producto {licores.nombre} s / n')
                if confirmacion == 's':
                    licoresList.remove(licores)
                    print(f'El producto {licores.nombre} se elimino correctamente')
                existeElPeluche = True
        if existeElPeluche == False:
            print("El producto no existe")

    #_______________________________MOSTRAR PRODUCTOS___________________________________


    elif opcion == 5:   #Mostrar inventario
        print("-------------Lacteos--------")
        for lacteo in lacteosList:
            print(lacteo.__str__())
        
        print("-------------Detergentes--------")
        for detergente in detergentesList:
            print(detergente.__str__())
        
        print("-------------Licores-------------")
        for licores in licoresList:
            print(licores.__str__())
    
    elif opcion == 6:
        print("Gracias totales")
        break
    else:
        print("Opción invalida")

    #_______________________________HERENCIA MULTIPLE___________________________________

class FigurasGeometricas:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def infoPapa1(self):
        print("Soy Figura Geométrica")

figura = FigurasGeometricas(3,4)
figura.info()

class Color:
    def __init__(self,color):
        self.color = color

    def infoPapa2(self):
        print("Soy un color")

color = Color ('Blue')
color.info()

class Cuadrado(FigurasGeometricas, Color):
    def __init__(self, alto, ancho, color):
        FigurasGeometricas.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def info(self):
        print("Soy un cuadrado")

    def area(self):
        return self.alto * self.ancho

cuadrado = Cuadrado (4,6,'rojo')
print(cuadrado.alto)
print(cuadrado.ancho)
print(cuadrado.color)
cuadrado.info()
cuadrado.infoPapa1()
cuadrado.infoPapa2()
print(cuadrado.area())

#_______________________________POLIMORFISMO___________________________________

class Animal:                       #Padre, Primaria, superclase
    def __init__(self,nombre):
        self.nombre = nombre

    def sonido(self):
        return "Error - las subclases son las que tienen sonido"

    def imprimirSonido(self):
        return self.sonido()

class Gato(Animal):             #Clase hija, subclase, derivada
    def __init__(self,nombre):
        super().__init__(nombre)

    def sonido(self):
        return "Miau Miau"

class Perro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)

    def sonido(self):
        return "Guau Guau"

gato1 = Gato("Jackie")
gatoFelix = Gato("Jackie")
perro1 = Perro("Cheese")

print(gato1.sonido())
print(perro1.sonido())
print(gato1.imprimirSonido())

animal = Animal("Pepe")
print(animal.sonido())
animal.imprimirSonido()








