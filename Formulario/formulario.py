from operator import index
from tkinter import NSEW, Tk, Label, Button, Entry, Frame, END, font
from turtle import width
import pandas as pd

formulario = Tk()
formulario.config(bg="cyan")
formulario.geometry("560x388")
formulario.resizable(0,0)
formulario.title("Formulario python por Eduardo")

nombre1,carrera1,edad1,correo1,telefono1 =[],[],[],[],[]
def agregar_datos():
    global nombre1, carrera1, dni1, correo1, telefono1

    nombre1.append(ingresa_nombre.get())
    carrera1.append(ingresa_carrera.get())
    edad1.append(ingresa_edad.get())
    correo1.append(ingresa_correo.get())
    telefono1.append(ingresa_telefono.get())

    ingresa_nombre.delete(0,END)
    ingresa_carrera.delete(0,END)
    ingresa_edad.delete(0,END)
    ingresa_correo.delete(0,END)
    ingresa_telefono.delete(0,END)

def guardar_datos():
    global nombre1,carrera1,edad1,correo1,telefono1

    datos= {"nombres": nombre1, "carrera": carrera1, "edad":edad1, "correo":correo1, "telefono": telefono1}
    nom_excel = str(nombre_archivo.get()+ ".xlsx")
    df = pd.DataFrame(datos,columns = ["nombres","carrera","edad","correo","telefono"])
    df.to_excel(nom_excel)
    nombre_archivo.delete(0,END)


frame1 = Frame(formulario, bg= "cyan")
frame1.grid(column=0, row=0, sticky="nsew")
frame2 = Frame(formulario, bg= "cyan")
frame2.grid(column=1, row=0, sticky="nsew")

nombre = Label(frame1, text="Nombre", widt=10, background="green").grid(column=0, row=0, pady=20, padx=20)
ingresa_nombre = Entry (frame1, width=20, font=("Arial",12))
ingresa_nombre.grid (column=1, row=0)

carrera = Label(frame1, text="Carrera", widt=10, background="green").grid(column=0, row=1, pady=20, padx=10)
ingresa_carrera = Entry (frame1, width=20, font=("Arial",12))
ingresa_carrera.grid (column=1, row=1)

edad = Label(frame1, text="Edad", widt=10, background="green").grid(column=0, row=2, pady=20, padx=10)
ingresa_edad = Entry (frame1, width=20, font=("Arial",12))
ingresa_edad.grid (column=1, row=2)

correo = Label(frame1, text="Correo", widt=10, background="green").grid(column=0, row=3, pady=20, padx=10)
ingresa_correo = Entry (frame1, width=20, font=("Arial",12))
ingresa_correo.grid (column=1, row=3)

telefono = Label(frame1, text="Telefono", widt=10, background="green").grid(column=0, row=4, pady=20, padx=10)
ingresa_telefono = Entry (frame1, width=20, font=("Arial",12))
ingresa_telefono.grid (column=1, row=4)

agregar = Button(frame1, width=20, font =("Arial", 12, "bold"), text= "Agregar", bg="red", bd=5, command= agregar_datos)

agregar.grid(columnspan=2, row=5, pady=20, padx=10)

archivo= Label(frame2, text="Ingrese Nombre del archivo", width=25, bg="cyan", font=("Arial",12, "bold"), fg="white")
archivo.grid(column=0, row=0, pady=10, padx=10)

nombre_archivo = Entry(frame2, width=23, font =("Arial", 12, "bold"), highlightbackground= "cyan", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=0, padx=10)

guardar= Button(frame2, width=20, font =("Arial", 12, "bold"), text= "Guardar", bg="red", bd=5, command = guardar_datos)
guardar.grid(column=0, row=2, pady=0, padx=10)

formulario.mainloop()

