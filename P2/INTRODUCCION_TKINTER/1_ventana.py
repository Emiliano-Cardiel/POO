'''
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
'''
#1er Forma
from tkinter import *

ventana=Tk()

#2nda Forma
# import tkinter as tk

# ventana=tk.Tk()

ventana.title("Mi primer app con Tkinter")
ventana.geometry("800x600")
ventana.mainloop() #Metodo que permite tener la ventana abierta todo el tiempo que dure la aplicación activa