from tkinter import *

ventana=Tk()
ventana.title("Marcos o Frame en Tkinter")
ventana.geometry("800x600")
ventana.resizable(False,False) #No pueda modificarse el tamaño de la ventana

marco1=Frame(ventana,width=400,height=200,bg="blue", relief=SOLID,border=2)
marco1.pack_propagate(False) #Evitar que se modifique el estilo del marco original
marco1.pack(pady=150) #Importante para que se dibuje o muestre el widget o el objeto dentro de la ventana
marco2=Frame(marco1,width=300,height=150,bg="silver",relief=GROOVE,border=10).pack(pady=50)


ventana.mainloop()