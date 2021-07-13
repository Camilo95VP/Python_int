from tkinter import *
from tkinter import messagebox

#funciones


class Peluche():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre,
        self.cantidad = cantidad,
        self.precio = precio


def agregar():
    if nombrePeluche.get() != "": 
        peluche = Peluche(nombre = nombrePeluche.get(), cantidad = cantidadPeluche.get(), precio = precioPeluche.get())
        pelucheList.append(peluche)
        messagebox.showinfo("Agregado", f'{nombrePeluche.get()} agregado correctamente')
        # limpiar()
        print(pelucheList)
    else:
        messagebox.showerror("Error", 'Primero debe llenar todos los campos')
   

def limpiar():
    nombrePeluche.set("")
    cantidadPeluche.set(0)
    precioPeluche.set(0.0)

#UI
ventana = Tk()
nombrePeluche = StringVar()
cantidadPeluche = IntVar()
precioPeluche = DoubleVar()
pelucheList = []

ventana.geometry("400x400")
ventana.title("Peluchitos.com")
tituloLabel = Label(ventana, text="Peluchitos.com").place(relx=0.5, y=10, anchor=CENTER)
nombreLabel = Label(ventana, text="Nombre del Peluche: ").place(x=10, y=40)
nombreEntry = Entry(ventana, textvariable=nombrePeluche).place(x=160, y=40)
cantidadLabel = Label(ventana, text="Cantidad del Peluche: ").place(x=10, y=70)
cantidadEntry = Entry(ventana, textvariable=cantidadPeluche).place(x=160, y=70)
precioLabel = Label(ventana, text="Precio del Peluche: ").place(x=10, y=100)
precioEntry = Entry(ventana, textvariable=precioPeluche).place(x=160, y=100)
AgregarButton = Button(ventana, text="Agregar", command=agregar).place(x=10, y=130)
ActualizarButton = Button(ventana, text="Limpiar", command=limpiar).place(x=70, y=130)
ventana.mainloop()
