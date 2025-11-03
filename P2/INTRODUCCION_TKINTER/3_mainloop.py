from tkinter import *

ventana=Tk()
ventana.title("Uso del Mainloop")
ventana.geometry("600x400")

marco1=Frame(ventana,width=600,height=50,bg="#FF0000",border=2,relief=RAISED).pack()
marco2=Frame(ventana,width=600,height=50,bg="#FF6600",border=2,relief=RAISED).pack()
marco3=Frame(ventana,width=600,height=50,bg="yellow",border=2,relief=RAISED).pack()
marco4=Frame(ventana,width=600,height=50,bg="green",border=2,relief=RAISED).pack()
marco5=Frame(ventana,width=600,height=50,bg="blue",border=2,relief=RAISED).pack()
marco6=Frame(ventana,width=600,height=50,bg="purple",border=2,relief=RAISED).pack()



ventana.mainloop()


