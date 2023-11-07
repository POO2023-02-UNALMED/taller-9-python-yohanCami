from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
#root.geometry("600x400")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

def pantalla0():
 
    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "0")


def pantalla1():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "1")

def pantalla2():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "2")

def pantalla3():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "3")

def pantalla4():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "4")

def pantalla5():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "5")

def pantalla6():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "6")

def pantalla7():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "7")

def pantalla8():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "8")

def pantalla9():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + "9")

def pantallaSum():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + " + ")

def pantallaRes():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + " - ")

def pantallaMul():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + " * ")

def pantallaDiv():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + " / ")

def pantallaPunto():

    anterior = pantalla.get()
    pantalla.delete(0, "end")  # Limpiar la entrada actual
    pantalla.insert(0, anterior + ".")

def pantallaIgual():

    anterior = pantalla.get()
    datos = anterior.split()
    pantalla.delete(0, "end")  # Limpiar la entrada actual

    entero =  True

    for i in datos:

        if "." in i:
            entero = False

    if entero:

        if datos[1] == "+":

            resultado = int(datos[0]) + int(datos[2])

        elif datos[1] == "-":

            resultado = int(datos[0]) - int(datos[2])

        elif datos[1] == "*":

            resultado = int(datos[0]) * int(datos[2])

        elif datos[1] == "/":

            resultado = int(datos[0]) / int(datos[2])

        pantalla.insert(0, resultado)

    else:

        if datos[1] == "+":

            resultado = float(datos[0]) + float(datos[2])

        elif datos[1] == "-":

            resultado = float(datos[0]) - float(datos[2])

        elif datos[1] == "*":

            resultado = float(datos[0]) * float(datos[2])

        elif datos[1] == "/":

            resultado = float(datos[0]) / float(datos[2])

        pantalla.insert(0, resultado)

# Configuración botones
boton_1 = Button(root, command=pantalla1, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, command=pantalla2, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, command=pantalla3, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, command=pantalla4, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, command=pantalla5, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, command=pantalla6, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, command=pantalla7, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, command=pantalla8, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, command=pantalla9, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, command=pantallaIgual, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, command=pantallaPunto, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, command=pantallaSum , text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, command=pantallaRes, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, command=pantallaMul, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, command=pantallaDiv,text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()