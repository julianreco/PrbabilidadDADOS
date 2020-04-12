from tkinter import *
import re
import math
from tkinter import messagebox
import random

from pygame import mixer# Load the required library

mixer.init()
mixer.music.load('.\soviet-anthem-8-bit.mp3')
mixer.music.play()

window = Tk()

window.title("ValueBets")

window.geometry('900x700')

lbl = Label(window, text = "Ingrese su Saldo: ")

lbl.grid()

txt = Entry(window, width = 15)

txt.grid()

lbl2 = Label(window, text = "Ingrese su Apuesta: ")

lbl2.grid()

txt2 = Entry(window, width = 15)

txt2.grid()

lbl3 = Label(window, text = "Tu Saldo es de: ")

lbl3.grid()

lbl4 = Label(window, text = "Tu Apuesta Actual es: ")

lbl4.grid()

lbl5 = Label(window, text = "Ingrese la Probabilidad de Ganar: ")

lbl5.grid()

txt5 = Entry(window, width = 15)

txt5.grid()

lbl6 = Label(window, text = "La probabilidad de ganar es: ")

lbl6.grid()

lbl7 = Label(window, text = "La Couta de Apuesta es: ")

lbl7.grid()

lbl8 = Label(window, text = "Dados", font = ("TimesNewRoman Bold", 25))

lbl8.grid()

lbl9 = Label(window, text = "Ingrese el numero de la Cara del Dado: ")

lbl9.grid()

txt9 = Entry(window, width = 3)

txt9.grid()

Image = PhotoImage(file = "img/dado.png")
Lbl_7 = Label(width = 390, image = Image)
Lbl_7.grid()
Lbl_7.place(x = 250, y = 230)

Image1 = PhotoImage(file = "img/1.png")
Lbl_1 = Label(width = 390, image = Image1)
Lbl_1.grid()
Lbl_1.place(x = 250, y = 230)
Lbl_1.place_forget()

Image2 = PhotoImage(file = "img/2.png")
Lbl_2 = Label(width = 390, image = Image2)
Lbl_2.grid()
Lbl_2.place(x = 250, y = 230)
Lbl_2.place_forget()

Image3 = PhotoImage(file = "img/3.png")
Lbl_3 = Label(width = 390, image = Image3)
Lbl_3.grid()
Lbl_3.place(x = 250, y = 230)
Lbl_3.place_forget()

Image4 = PhotoImage(file = "img/4.png")
Lbl_4 = Label(width = 390, image = Image4)
Lbl_4.grid()
Lbl_4.place(x = 250, y = 230)
Lbl_4.place_forget()

Image5 = PhotoImage(file = "img/5.png")
Lbl_5 = Label(width = 390, image = Image5)
Lbl_5.grid()
Lbl_5.place(x = 250, y = 230)
Lbl_5.place_forget()

Image6 = PhotoImage(file = "img/6.png")
Lbl_6 = Label(width = 390, image = Image6)
Lbl_6.grid()
Lbl_6.place(x = 250, y = 230)
Lbl_6.place_forget()

saldo = 0
va = 0
pg = 0.0
ca = 0.0
caradado = 0

def clicked():

  if re.search("^[0-9]+([,][0-9]+)?$", txt.get()) == None:
  messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
else :
  global saldo
saldo = int(txt.get())
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
desbtn()

def clickedapuesta():

  if re.search("^[0-9]+([,][0-9]+)?$", txt2.get()) == None:
  messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
else :
  global va
va = int(txt2.get())
if va > saldo:
  messagebox.showwarning(
    'Advertencia', 'El valor apostado es mayor al saldo')
else :
  res = "Tu Apuesta Actual es: " + str(va)
lbl4.configure(text = res)
desbtnapuesta()

def clickedprobabilidad():

  if re.search("^[0-9]+([.][0-9]+)?$", txt5.get()) == None:
  messagebox.showwarning('Advertencia', 'Ingrese solo probabilidades de 0 a 1')
else :
  global pg
pg = float(txt5.get())
if pg < 0.0 or pg > 1.0:
  messagebox.showwarning('Advertencia', 'Ingrese valores de 0 a 1')
else :
  res = "Probabilidad de Ganar es: " + str(pg)
lbl6.configure(text = res)
desbtnprobabilidad()
cuotaglobal()
if pg == 0:
  print("puto el que lo lea")
elif pg > 0 and pg < 0.1: #caradado = numramd entre 100
elif pg >= 0.1 and pg < 0.16: #caradado = numramd entre 10
elif pg >= 0.16 and pg < 0.33: #caradado
elif pg >= 0.33 and pg < 0.5: #caradado numrand rango 2
elif pg >= 0.5 and pg < 0.66: #pares e impares
elif pg >= 0.66 and pg < 0.83: #caradado numrand rango 4
elif pg >= 0.83 and pg <= 0.99: #caradado numrand rango 5
elif pg == 1: #gana

def cuotaglobal():
  global ca
ca = round(float(1 / pg), 2)
res = "Couta de Apuesta es: " + str(ca)
lbl7.configure(text = res)

def clickedcaradado():
  if re.search("^[0-9]+([,][0-9]+)?$", txt.get()) == None:
  messagebox.showwarning('Advertencia', 'Ingrese solo numeros enteros')
else :
  global caradado
caradado = int(txt9.get())
if caradado >= 1 and caradado <= 6:
  desbtndado()
else :
  messagebox.showwarning(
    'Advertencia', 'Ingrese solo caras del dado')

def juegodado():
  global caradado, saldo, ca, va, Lbl_7, Lbl_6, Lbl_5, Lbl_4, Lbl_3, Lbl_2, Lbl_1
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
Lbl_1.place(x = 250, y = 280)
if cara == 2:
  Lbl_7.place_forget()
Lbl_2.grid()
Lbl_2.place(x = 250, y = 280)
if cara == 3:
  Lbl_7.place_forget()
Lbl_3.grid()
Lbl_3.place(x = 250, y = 280)
if cara == 4:
  Lbl_7.place_forget()
Lbl_4.grid()
Lbl_4.place(x = 250, y = 280)
if cara == 5:
  Lbl_7.place_forget()
Lbl_5.grid()
Lbl_5.place(x = 250, y = 280)
if cara == 6:
  Lbl_7.place_forget()
Lbl_6.grid()
Lbl_6.place(x = 250, y = 280)
if cara == caradado:
  messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
saldonuevo = saldo - va + (va * ca)
saldo = round(saldonuevo)
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
ca = 0
va = 0
caradado = 0
desblqdado()
else :
  messagebox.showwarning('Perdiste', 'Felicidades ahora es nuestro dinero')
saldonuevo = saldo - va
saldo = saldonuevo
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
ca = 0
va = 0
caradado = 0
desblqdado()

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
Lbl_1.place(x = 250, y = 280)
if cara == 2:
  Lbl_7.place_forget()
Lbl_2.grid()
Lbl_2.place(x = 250, y = 280)
if cara == 3:
  Lbl_7.place_forget()
Lbl_3.grid()
Lbl_3.place(x = 250, y = 280)
if cara == 4:
  Lbl_7.place_forget()
Lbl_4.grid()
Lbl_4.place(x = 250, y = 280)
if cara == 5:
  Lbl_7.place_forget()
Lbl_5.grid()
Lbl_5.place(x = 250, y = 280)
if cara == 6:
  Lbl_7.place_forget()
Lbl_6.grid()
Lbl_6.place(x = 250, y = 280)
if cara % 2 == 0:
  messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
saldonuevo = saldo - va + (va * ca)
saldo = saldonuevo
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
ca = 0
va = 0
desblqdado()
else :
  messagebox.showwarning('Perdiste', 'Felicidades ahora es nuestro dinero')
saldonuevo = saldo - va
saldo = saldonuevo
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
ca = 0
va = 0
desblqdado()

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
Lbl_1.place(x = 250, y = 280)
if cara == 2:
  Lbl_7.place_forget()
Lbl_2.grid()
Lbl_2.place(x = 250, y = 280)
if cara == 3:
  Lbl_7.place_forget()
Lbl_3.grid()
Lbl_3.place(x = 250, y = 280)
if cara == 4:
  Lbl_7.place_forget()
Lbl_4.grid()
Lbl_4.place(x = 250, y = 280)
if cara == 5:
  Lbl_7.place_forget()
Lbl_5.grid()
Lbl_5.place(x = 250, y = 280)
if cara == 6:
  Lbl_7.place_forget()
Lbl_6.grid()
Lbl_6.place(x = 250, y = 280)
if cara % 2 != 0:
  messagebox.showinfo('Ganaste', 'Felicidades has ganado 3 nukes')
saldonuevo = saldo - va + (va * ca)
saldo = saldonuevo
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
ca = 0
va = 0
desblqdado()
else :
  messagebox.showwarning('Perdiste', 'Felicidades ahora es nuestro dinero')
saldonuevo = saldo - va
saldo = saldonuevo
res = "Tu Saldo es de: " + str(saldo)
lbl3.configure(text = res)
ca = 0
va = 0
desblqdado()

btnsaldo = Button(window, text = "Confirmar", command = clicked, padx = 5)
btnapuesta = Button(window, text = "Confirmar", command = clickedapuesta, padx = 5)
btnprobabilidad = Button(window, text = "Confirmar",
  command = clickedprobabilidad, padx = 5)
btncaradado = Button(window, text = "Confirmar", command = clickedcaradado, padx = 5)
btncaradadopar = Button(window, text = "Caras Pares",
  command = juegodadopar, padx = 5)
btncaradadoimpar = Button(window, text = "Caras Impares",
  command = juegodadoimpar, padx = 5)
btnjugardado = Button(window, text = "Cara individual",
  command = juegodado, padx = 5)

def desbtn():

  btnsaldo.config(state = 'disabled')

def desbtnapuesta():

  btnapuesta.config(state = 'disabled')

def desbtnprobabilidad():

  btnprobabilidad.config(state = 'disabled')

def desbtndado():

  btncaradado.config(state = 'disabled')
btncaradadopar.config(state = 'disabled')
btncaradadoimpar.config(state = 'disabled')

def desblqdado():
  btncaradado.config(state = 'normal')
btncaradadopar.config(state = 'normal')
btncaradadoimpar.config(state = 'normal')
btnapuesta.config(state = 'normal')
btnprobabilidad.config(state = 'normal')

def despareimpar():
  btncaradadopar.config(state = 'disabled')
btncaradadoimpar.config(state = 'disabled')

btnapuesta.place(x = 210, y = 130)
btnsaldo.place(x = 210, y = 100)
btnprobabilidad.place(x = 290, y = 170)
btncaradado.place(x = 290, y = 210)
btncaradadopar.place(x = 310, y = 650)
btncaradadoimpar.place(x = 530, y = 650)
btnjugardado.place(x = 410, y = 650)
lbl.place(x = 0, y = 100)# saldo
txt.place(x = 108, y = 100)# saldo
txt2.place(x = 108, y = 130)# apuesta
lbl2.place(x = 0, y = 130)# apuesta
lbl4.place(x = 690, y = 120)# saldo
lbl3.place(x = 690, y = 100)# apuesta
lbl5.place(x = 0, y = 170)# probabilidad
lbl6.place(x = 690, y = 160)# probabilidad
lbl7.place(x = 690, y = 180)# Cuota
txt5.place(x = 185, y = 170)# probabilidadtxt
lbl8.place(x = 410, y = 20)# dados
lbl9.place(x = 20, y = 210)# cara dados
txt9.place(x = 235, y = 210)# cara dados

# btnsaldo.grid(column = 3, row = 0, columnspan = 4)

window.mainloop()