from tkinter import *
import re
import math
from tkinter import messagebox
import random
import time

from pygame import mixer  # Load the required library

from Graficas import *

mixer.init()
mixer.music.load('.\soviet-anthem-8-bit.mp3')
mixer.music.play()

window = Tk()

window.title("ValueBets")

window.geometry('900x700')

lbl = Label(window, text="Ingrese su Saldo: ")

lbl.grid()

txt = Entry(window, width=15)

txt.grid()

lbl2 = Label(window, text="Ingrese su Apuesta: ")

lbl2.grid()

txt2 = Entry(window, width=15)

txt2.grid()

lbl3 = Label(window, text="Tu Saldo es de: ")

lbl3.grid()

lbl4 = Label(window, text="Tu Apuesta Actual es: ")

lbl4.grid()

lbl5 = Label(window, text="Ingrese la Probabilidad de Ganar: ")

lbl5.grid()

txt5 = Entry(window, width=15)

txt5.grid()

lbl6 = Label(window, text="La probabilidad de ganar es: ")

lbl6.grid()

lbl7 = Label(window, text="La Couta de Apuesta es: ")

lbl7.grid()

lbl8 = Label(window, text="Dados", font=("TimesNewRoman Bold", 25))

lbl8.grid()

lbl9 = Label(window, text="Ingrese el numero de la Cara del Dado: ")

txt9 = Entry(window, width=2)

lbl10 = Label(window, text="Modalidad de juego: ")

lbl10.grid()

lbl11 = Label(window, text="Ingrese el numero de la Cara#2 del Dado: ")

txt11 = Entry(window, width=2)

lbl12 = Label(window, text="Ingrese el numero de la Cara#3 del Dado: ")

txt12 = Entry(window, width=2)

lbl13 = Label(window, text="Ingrese el numero de la Cara#4 del Dado: ")

txt13 = Entry(window, width=2)

lbl14 = Label(window, text="Ingrese el numero de la Cara#5 del Dado: ")

txt14 = Entry(window, width=2)

lbl11.place_forget()

txt11.place_forget()

lbl12.place_forget()

txt12.place_forget()

lbl13.place_forget()

txt13.place_forget()

lbl14.place_forget()

txt14.place_forget()

Image = PhotoImage(file="img/dado.png")
Lbl_7 = Label(width=390, image=Image)
Lbl_7.grid()
Lbl_7.place(x=250, y=230)


Image1 = PhotoImage(file="img/1.png")
Lbl_1 = Label(width=390, image=Image1)
Lbl_1.grid()
Lbl_1.place(x=250, y=230)
Lbl_1.place_forget()

Image2 = PhotoImage(file="img/2.png")
Lbl_2 = Label(width=390, image=Image2)
Lbl_2.grid()
Lbl_2.place(x=250, y=230)
Lbl_2.place_forget()

Image3 = PhotoImage(file="img/3.png")
Lbl_3 = Label(width=390, image=Image3)
Lbl_3.grid()
Lbl_3.place(x=250, y=230)
Lbl_3.place_forget()

Image4 = PhotoImage(file="img/4.png")
Lbl_4 = Label(width=390, image=Image4)
Lbl_4.grid()
Lbl_4.place(x=250, y=230)
Lbl_4.place_forget()

Image5 = PhotoImage(file="img/5.png")
Lbl_5 = Label(width=390, image=Image5)
Lbl_5.grid()
Lbl_5.place(x=250, y=230)
Lbl_5.place_forget()

Image6 = PhotoImage(file="img/6.png")
Lbl_6 = Label(width=390, image=Image6)
Lbl_6.grid()
Lbl_6.place(x=250, y=230)
Lbl_6.place_forget()

apuesta = 0
saldo = 0
va = 0
pg = 0.0
ca = 0.0
caradado = 0
caradado_1 = 0
caradado_2 = 0
caradado_3 = 0
caradado_4 = 0
caradado_5 = 0


def clicked():

    if re.search("^[0-9]+([,][0-9]+)?$", txt.get()) == None:
        messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
    else:
        global saldo,data2
        saldo = int(txt.get())
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        desbtn()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        y = data2.get('Apuesta')
        y.append(apuesta)
        data2.update({'Apuesta':y})



def clickedapuesta():

    if re.search("^[0-9]+([,][0-9]+)?$", txt2.get()) == None:
        messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
    else:
        global va,apuesta
        va = int(txt2.get())
        if va > saldo:
            messagebox.showwarning(
                'Advertencia', 'El valor apostado es mayor al saldo')
        else:
            res = "Tu Apuesta Actual es: " + str(va)
            lbl4.configure(text=res)
            desbtnapuesta()
            apuesta+=1
            x = data2.get('Apuesta')
            x.append(apuesta)
            data2.update({'Apuesta':x})
            


def clickedprobabilidad():
    if re.search("^[0-9]+([.][0-9]+)?$", txt5.get()) == None:
        messagebox.showwarning(
            'Advertencia', 'Ingrese solo probabilidades de 0 a 1')
    else:
        global pg, btnjugardado
        pg = float(txt5.get())
        if pg < 0.0 or pg > 1.0:
            messagebox.showwarning('Advertencia', 'Ingrese valores de 0 a 1')

        if pg == 0:
            res = "Modalidad de juego: \n Probabilidad de ganar es 0% \n es el fin de la USSR :("
            btncuatrocaras.place_forget()
            btncincocaras.place_forget()
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget() 
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            botonescaraind()
            lbl10.configure(text=res)
            despareimpar()
        elif pg > 0 and pg < 0.1:
            res = "Modalidad de juego: \n La cara a elegir debe ser igual \n a un numero aleatorio \n entre 1 y 100"
            lbl10.configure(text=res)
            btncuatrocaras.place_forget()
            despareimpar()
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget() 
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            botonescaraind()
        elif pg >= 0.1 and pg < 0.16:
            res = "Modalidad de juego: \n La cara a elegir debe ser igual \n a un numero aleatorio \n entre 1 y 10"
            lbl10.configure(text=res)
            btncuatrocaras.place_forget()
            despareimpar()
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget() 
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            botonescaraind()
        elif pg >= 0.16 and pg < 0.305:
            res = "Modalidad de juego: \n La cara a elegir debe ser \n una de las 6 caras de un dado \n que creas que va a caer"
            lbl10.configure(text=res)
            btncuatrocaras.place_forget()
            despareimpar()
            botonescaraind()
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget()           
        elif pg >= 0.305 and pg < 0.5:
            res = "Modalidad de juego: \n se tiraran dos veces los dados \n la cara a seleccionar debe ser \n almenos uno de los resultados"
            lbl10.configure(text=res)
            btncuatrocaras.place_forget()
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget() 
            despareimpar()
            botonescaraind()
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
        elif pg >= 0.5 and pg < 0.66:
            res = "Modalidad de juego: \n la cara del dado \n debe ser par o impar"
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget()
            btncaradado.place_forget()
            btncuatrocaras.place_forget()
            btnjugardado.place_forget()
            lbl9.place_forget()
            txt9.place_forget()
            lbl10.configure(text=res)
            botonesparesimpares()
            desblqpareimpar()
        elif pg >= 0.66 and pg < 0.83:
            res = "Modalidad de juego: \n puede escoger 4 caras del dado \n almenos debe tener una cara \n correcta para ganar"
            lbl14.place_forget()
            txt14.place_forget()
            btncaradado.place_forget()
            cuatrocaras()
            btncaradadopar.place_forget()
            btncaradadoimpar.place_forget()
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            txt11.grid()
            lbl11.grid()
            lbl11.place(x=10, y=230)
            txt11.place(x=235, y=230)
            txt12.grid()
            lbl12.grid()
            lbl12.place(x=10, y=250)
            txt12.place(x=235, y=250)
            txt13.grid()
            lbl13.grid()
            lbl13.place(x=10, y=270)
            txt13.place(x=235, y=270)
            lbl10.configure(text=res)
            despareimpar()
            jugar()
        elif pg >= 0.83 and pg <= 0.99:
            res = "Modalidad de juego: \n puede escoger 5 caras del dado \n almenos debe tener una cara \n correcta para ganar"
            btncuatrocaras.place_forget()
            btncaradado.place_forget()
            btncaradadopar.place_forget()
            btncaradadoimpar.place_forget()
            cincocaras()
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            txt11.grid()
            lbl11.grid()
            lbl11.place(x=10, y=230)
            txt11.place(x=235, y=230)
            txt12.grid()
            lbl12.grid()
            lbl12.place(x=10, y=250)
            txt12.place(x=235, y=250)
            txt13.grid()
            lbl13.grid()
            lbl13.place(x=10, y=270)
            txt13.place(x=235, y=270)
            txt14.grid()
            lbl14.grid()
            lbl14.place(x=10, y=290)
            txt14.place(x=235, y=290)
            lbl10.configure(text=res)
            despareimpar()
            jugar()
        elif pg == 1:
            res = "Modalidad de juego: \n siempre se gana"
            btncuatrocaras.place_forget()
            btncaradadopar.place_forget()
            btncaradadoimpar.place_forget()
            btncincocaras.place_forget()
            lbl11.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl14.place_forget()
            txt11.place_forget()
            txt12.place_forget()
            txt13.place_forget()
            txt14.place_forget() 
            txt9.grid()
            lbl9.grid()
            lbl9.place(x=10, y=210)
            txt9.place(x=235, y=210)
            botonescaraind()
            lbl10.configure(text=res)
            despareimpar()
        res = "Probabilidad de Ganar es: " + str(pg)
        lbl6.configure(text=res)
        desbtnprobabilidad()
        cuotaglobal()

def cuotaglobal():
    global ca
    ca = round(float(1/pg), 2)
    res = "Couta de Apuesta es: " + str(ca)
    lbl7.configure(text=res)


def clickedcaradado():
    if re.search("^[0-9]+([,][0-9]+)?$", txt.get()) == None:
        messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
    else:
        global caradado
        caradado = int(txt9.get())
        if caradado >= 1 and caradado <= 6:
            desbtndado()
        else:
            messagebox.showwarning(
                'Advertencia', 'Ingrese solo caras del dado')


def clickedcara2():
    if re.search("^[0-9]+([,][0-9]+)?$", txt.get()) == None:
        messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
    else:
        global caradado
        caradado = int(txt9.get())
        if caradado >= 1 and caradado <= 6:
            desbtndado()
        else:
            messagebox.showwarning(
                'Advertencia', 'Ingrese solo caras del dado')


def juegodado():
    global caradado, saldo, ca, va, Lbl_7, Lbl_6, Lbl_5, Lbl_4, Lbl_3, Lbl_2, Lbl_1,data2
    Lbl_1.place_forget()
    Lbl_2.place_forget()
    Lbl_3.place_forget()
    Lbl_4.place_forget()
    Lbl_5.place_forget()
    Lbl_6.place_forget()
    global pg, caradado_1, caradado_2, caradado_3, caradado_4, caradado_5, btnjugardado
    pg = float(txt5.get())
    if pg < 0.0 or pg > 1.0:
        messagebox.showwarning('Advertencia', 'Ingrese valores de 0 a 1')

    if pg == 0:
        res = "Modalidad de juego: \n Probabilidad de ganar es 0% \n es el fin de la USSR :("
        txt9.grid()
        lbl9.grid()
        lbl9.place(x=10, y=210)
        txt9.place(x=235, y=210)
        cara = int(txt9.get())
        if cara != 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara != 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara != 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara != 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara != 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara != 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        messagebox.showwarning(
            'Perdiste', 'Felicidades ahora es nuestro dinero')
        saldonuevo = saldo - va
        saldo = saldonuevo
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        ca = 0
        va = 0
        desblqdado()
        botonescaraind()
        lbl10.configure(text=res)
        despareimpar()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        graficar()
    elif pg > 0 and pg < 0.1:
        res = "Modalidad de juego: \n La cara a elegir debe ser igual \n a un numero aleatorio \n entre 1 y 100"
        txt9.grid()
        lbl9.grid()
        lbl9.place(x=10, y=210)
        txt9.place(x=235, y=210)
        lbl10.configure(text=res)
        despareimpar()
        cara = random.randrange(1, 7)
        x = random.randrange(1,101)
        if cara == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        if cara == caradado:
            if cara == x:
                messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
                saldonuevo = saldo - va + (va * ca)
                saldo = round(saldonuevo)
                res = "Tu Saldo es de: " + str(saldo)
                lbl3.configure(text=res)
                ca = 0
                va = 0
                caradado = 0
                desblqdado()
                x = data2.get('Saldo')
                x.append(saldo)
                data2.update({'Saldo':x})
                graficar()
            else:
                messagebox.showwarning('Perdiste', 'Felicidades ahora es nuestro dinero')
                saldonuevo = saldo - va
                saldo = saldonuevo
                res = "Tu Saldo es de: " + str(saldo)
                lbl3.configure(text=res)
                ca = 0
                va = 0
                caradado = 0
                desblqdado()
                x = data2.get('Saldo')
                x.append(saldo)
                data2.update({'Saldo':x})
                graficar()
        else:
            messagebox.showwarning(
                'Perdiste', 'Felicidades ahora es nuestro dinero')
            saldonuevo = saldo - va
            saldo = saldonuevo
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
    elif pg >= 0.1 and pg < 0.16:
        res = "Modalidad de juego: \n La cara a elegir debe ser igual \n a un numero aleatorio \n entre 1 y 10"
        txt9.grid()
        lbl9.grid()
        lbl9.place(x=10, y=210)
        txt9.place(x=235, y=210)
        lbl10.configure(text=res)
        despareimpar()
        cara = random.randrange(1, 7)
        x = random.randrange(1,11)
        if cara == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        if cara == caradado:
            if cara == x:
                messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
                saldonuevo = saldo - va + (va * ca)
                saldo = round(saldonuevo)
                res = "Tu Saldo es de: " + str(saldo)
                lbl3.configure(text=res)
                ca = 0
                va = 0
                caradado = 0
                desblqdado()
                x = data2.get('Saldo')
                x.append(saldo)
                data2.update({'Saldo':x})
                graficar()
            else:
                messagebox.showwarning('Perdiste', 'Felicidades ahora es nuestro dinero')
                saldonuevo = saldo - va
                saldo = saldonuevo
                res = "Tu Saldo es de: " + str(saldo)
                lbl3.configure(text=res)
                ca = 0
                va = 0
                caradado = 0
                desblqdado()
                x = data2.get('Saldo')
                x.append(saldo)
                data2.update({'Saldo':x})
                graficar()
        else:
            messagebox.showwarning(
                'Perdiste', 'Felicidades ahora es nuestro dinero')
            saldonuevo = saldo - va
            saldo = saldonuevo
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
    elif pg >= 0.16 and pg < 0.305:
        cara = random.randrange(1, 7)
        if cara == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        if cara == caradado:
            messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
            saldonuevo = saldo - va + (va * ca)
            saldo = round(saldonuevo)
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
        else:
            messagebox.showwarning(
                'Perdiste', 'Felicidades ahora es nuestro dinero')
            saldonuevo = saldo - va
            saldo = saldonuevo
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
    elif pg >= 0.305 and pg < 0.5:
        res = "Modalidad de juego: \n se tiraran dos veces los dados \n la cara a seleccionar debe ser \n almenos uno de los resultados"
        lbl10.configure(text=res)
        despareimpar()
        cara1 = random.randrange(1, 7)
        cara2 = random.randrange(1, 7)
        if cara1 == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=200, y=280)
        if cara1 == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=200, y=280)
        if cara1 == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=200, y=280)
        if cara1 == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=200, y=280)
        if cara1 == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=200, y=280)
        if cara1 == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=200, y=280)
        if cara2 == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=550, y=280)
        if cara2 == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=550, y=280)
        if cara2 == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=550, y=280)
        if cara2 == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=550, y=280)
        if cara2 == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=550, y=280)
        if cara2 == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=550, y=280)
        if cara1 == caradado or cara2 == caradado:
            messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
            saldonuevo = saldo - va + (va * ca)
            saldo = round(saldonuevo)
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
        else:
            messagebox.showwarning(
                'Perdiste', 'Felicidades ahora es nuestro dinero')
            saldonuevo = saldo - va
            saldo = saldonuevo
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
    elif pg >= 0.66 and pg < 0.83:
        btncuatrocaras.config(state="normal")
        cara = random.randrange(1, 7)
        if cara == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        if cara == caradado_1 or cara == caradado_2 or cara == caradado_3 or cara == caradado_4:
            messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
            saldonuevo = saldo - va + (va * ca)
            saldo = round(saldonuevo)
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
        else:
            messagebox.showwarning(
                'Perdiste', 'Felicidades ahora es nuestro dinero')
            saldonuevo = saldo - va
            saldo = saldonuevo
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()        
    elif pg >= 0.83 and pg <= 0.99:
        res = "Modalidad de juego: \n puede escoger 5 caras del dado \n almenos debe tener una cara \n correcta para ganar"
        lbl10.configure(text=res)
        despareimpar()
        btncincocaras.config(state="normal")
        cara = random.randrange(1, 7)
        if cara == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        if cara == caradado_1 or cara == caradado_2 or cara == caradado_3 or cara == caradado_4 or cara == caradado_5:
            messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
            saldonuevo = saldo - va + (va * ca)
            saldo = round(saldonuevo)
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
        else:
            messagebox.showwarning(
                'Perdiste', 'Felicidades ahora es nuestro dinero')
            saldonuevo = saldo - va
            saldo = saldonuevo
            res = "Tu Saldo es de: " + str(saldo)
            lbl3.configure(text=res)
            ca = 0
            va = 0
            caradado = 0
            desblqdado()
            x = data2.get('Saldo')
            x.append(saldo)
            data2.update({'Saldo':x})
            graficar()
    elif pg == 1:
        res = "Modalidad de juego: \n siempre se gana"
        lbl10.configure(text=res)
        despareimpar()
        cara = int(txt9.get())
        if cara == 1:
            Lbl_7.place_forget()
            Lbl_1.grid()
            Lbl_1.place(x=250, y=280)
        if cara == 2:
            Lbl_7.place_forget()
            Lbl_2.grid()
            Lbl_2.place(x=250, y=280)
        if cara == 3:
            Lbl_7.place_forget()
            Lbl_3.grid()
            Lbl_3.place(x=250, y=280)
        if cara == 4:
            Lbl_7.place_forget()
            Lbl_4.grid()
            Lbl_4.place(x=250, y=280)
        if cara == 5:
            Lbl_7.place_forget()
            Lbl_5.grid()
            Lbl_5.place(x=250, y=280)
        if cara == 6:
            Lbl_7.place_forget()
            Lbl_6.grid()
            Lbl_6.place(x=250, y=280)
        messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
        saldonuevo = saldo - va + (va * ca)
        saldo = round(saldonuevo)
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        ca = 0
        va = 0
        caradado = 0
        desblqdado()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        graficar()
   

def juegodadopar():
    global saldo, ca, va, Lbl_7, Lbl_6, Lbl_5, Lbl_4, Lbl_3, Lbl_2, Lbl_1
    Lbl_1.place_forget()
    Lbl_2.place_forget()
    Lbl_3.place_forget()
    Lbl_4.place_forget()
    Lbl_5.place_forget()
    Lbl_6.place_forget()
    cara = random.randrange(1, 7)
    if cara == 1:
        Lbl_7.place_forget()
        Lbl_1.grid()
        Lbl_1.place(x=250, y=280)
    if cara == 2:
        Lbl_7.place_forget()
        Lbl_2.grid()
        Lbl_2.place(x=250, y=280)
    if cara == 3:
        Lbl_7.place_forget()
        Lbl_3.grid()
        Lbl_3.place(x=250, y=280)
    if cara == 4:
        Lbl_7.place_forget()
        Lbl_4.grid()
        Lbl_4.place(x=250, y=280)
    if cara == 5:
        Lbl_7.place_forget()
        Lbl_5.grid()
        Lbl_5.place(x=250, y=280)
    if cara == 6:
        Lbl_7.place_forget()
        Lbl_6.grid()
        Lbl_6.place(x=250, y=280)
    if cara % 2 == 0:
        messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
        saldonuevo = saldo - va + (va * ca)
        saldo = saldonuevo
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        ca = 0
        va = 0
        desblqdado()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        graficar()
    else:
        messagebox.showwarning(
            'Perdiste', 'Felicidades ahora es nuestro dinero')
        saldonuevo = saldo - va
        saldo = saldonuevo
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        ca = 0
        va = 0
        desblqdado()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        graficar()


def juegodadoimpar():
    global saldo, ca, va, Lbl_7, Lbl_6, Lbl_5, Lbl_4, Lbl_3, Lbl_2, Lbl_1
    Lbl_1.place_forget()
    Lbl_2.place_forget()
    Lbl_3.place_forget()
    Lbl_4.place_forget()
    Lbl_5.place_forget()
    Lbl_6.place_forget()
    cara = random.randrange(1, 7)
    if cara == 1:
        Lbl_7.place_forget()
        Lbl_1.grid()
        Lbl_1.place(x=250, y=280)
    if cara == 2:
        Lbl_7.place_forget()
        Lbl_2.grid()
        Lbl_2.place(x=250, y=280)
    if cara == 3:
        Lbl_7.place_forget()
        Lbl_3.grid()
        Lbl_3.place(x=250, y=280)
    if cara == 4:
        Lbl_7.place_forget()
        Lbl_4.grid()
        Lbl_4.place(x=250, y=280)
    if cara == 5:
        Lbl_7.place_forget()
        Lbl_5.grid()
        Lbl_5.place(x=250, y=280)
    if cara == 6:
        Lbl_7.place_forget()
        Lbl_6.grid()
        Lbl_6.place(x=250, y=280)
    if cara % 2 != 0:
        messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
        saldonuevo = saldo - va + (va * ca)
        saldo = saldonuevo
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        ca = 0
        va = 0
        desblqdado()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        graficar()
    else:
        messagebox.showwarning(
            'Perdiste', 'Felicidades ahora es nuestro dinero')
        saldonuevo = saldo - va
        saldo = saldonuevo
        res = "Tu Saldo es de: " + str(saldo)
        lbl3.configure(text=res)
        ca = 0
        va = 0
        desblqdado()
        x = data2.get('Saldo')
        x.append(saldo)
        data2.update({'Saldo':x})
        graficar()

def jhin():
    global caradado_1, caradado_2, caradado_3, caradado_4
    caradado_1 = int(txt9.get())
    caradado_2 = int(txt11.get())
    caradado_3 = int(txt12.get())
    caradado_4 = int(txt13.get())
    btncuatrocaras.config(state="disabled")

def cinko():
    global caradado_1, caradado_2, caradado_3, caradado_4, caradado_5
    caradado_1 = int(txt9.get())
    caradado_2 = int(txt11.get())
    caradado_3 = int(txt12.get())
    caradado_4 = int(txt13.get())
    caradado_4 = int(txt14.get())
    btncincocaras.config(state="disabled")




btnsaldo = Button(window, text="Confirmar", command=clicked, padx=5)
btncuatrocaras = Button(window, text="Confirmar", command=jhin, padx=5)
btncincocaras = Button(window, text="Confirmar", command=cinko, padx=5)
btnapuesta = Button(window, text="Confirmar", command=clickedapuesta, padx=5)
btnprobabilidad = Button(window, text="Confirmar",
                         command=clickedprobabilidad, padx=5)
btncaradado = Button(window, text="Confirmar", command=clickedcaradado, padx=5)
btncaradadopar = Button(window, text="Caras Pares",
                        command=juegodadopar, padx=5)
btncaradadoimpar = Button(window, text="Caras Impares",
                          command=juegodadoimpar, padx=5)
btnjugardado = Button(window, text="Jugar",
                      command=juegodado, padx=5)


def desbtn():

    btnsaldo.config(state='disabled')


def desbtnapuesta():

    btnapuesta.config(state='disabled')


def desbtnprobabilidad():

    btnprobabilidad.config(state='disabled')


def desbtndado():

    btncaradado.config(state='disabled')
    btncaradadopar.config(state='disabled')
    btncaradadoimpar.config(state='disabled')


def desblqdado():
    btncaradado.config(state='normal')
    btncaradadopar.config(state='normal')
    btncaradadoimpar.config(state='normal')
    btnapuesta.config(state='normal')
    btnprobabilidad.config(state='normal')


def desblqpareimpar():
    btncaradado.config(state='disabled')
    btncaradadopar.config(state='normal')
    btncaradadoimpar.config(state='normal')


def despareimpar():
    btncaradadopar.config(state='disabled')
    btncaradadoimpar.config(state='disabled')


def botonesparesimpares():
    btncaradadopar.place(x=310, y=650)
    btncaradadoimpar.place(x=530, y=650)


def botonescaraind():
    btncaradado.place(x=290, y=210)
    btnjugardado.place(x=410, y=650)

def jugar():
    btnjugardado.place(x=410, y=650)

def cuatrocaras():
    btncuatrocaras.place(x=290, y=210)

def cincocaras():
    btncincocaras.place(x=290, y=210)

btnapuesta.place(x=210, y=130)
btnsaldo.place(x=210, y=100)
btnprobabilidad.place(x=290, y=170)
#btncaradado.place(x=290, y=210)
#btncaradadopar.place(x=310, y=650)
#btncaradadoimpar.place(x=530, y=650)
#btnjugardado.place(x=410, y=650)
lbl.place(x=0, y=100)  # saldo
txt.place(x=108, y=100)  # saldo
txt2.place(x=108, y=130)  # apuesta
lbl2.place(x=0, y=130)  # apuesta
lbl4.place(x=690, y=120)  # saldo
lbl3.place(x=690, y=100)  # apuesta
lbl5.place(x=0, y=170)  # probabilidad
lbl6.place(x=690, y=160)  # probabilidad
lbl7.place(x=690, y=180)  # Cuota
txt5.place(x=185, y=170)  # probabilidadtxt
lbl8.place(x=410, y=20)  # dados
lbl10.place(x=10, y=320)  # modalidad


# btnsaldo.grid(column=3, row=0, columnspan=4)

window.mainloop()
