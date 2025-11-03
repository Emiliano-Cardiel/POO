from tkinter import *

ventana=Tk()

ventana.title("Labels")
ventana.geometry("600x400")

marco1=Frame(ventana,width=600,height=50,bg="#9FFCEF",border=3,relief=RIDGE)
marco1.pack_propagate(False)
marco1.pack()
marco2=Frame(ventana,width=600,height=50,bg="#108C7B",border=3,relief=FLAT)
marco2.pack_propagate(False)
marco2.pack(pady=25)
marco3=Frame(ventana,width=600,height=50,bg="#B823CB",border=3,relief=GROOVE)
marco3.pack_propagate(False)
marco3.pack(pady=25)
marco4=Frame(ventana,width=600,height=50,bg="#FA098D",border=3,relief=RAISED)
marco4.pack_propagate(False)
marco4.pack(pady=25)

etiqueta1=Label(marco1,text="Emiliano Arturo Cardiel Mares",bg="#9FFCEF").pack(pady=10)
etiqueta2=Label(marco2,text="Universidad Tecnológica de Durango",bg="#108C7B").pack(pady=10)
etiqueta3=Label(marco3,text="Tecnologías de la Información ",bg="#B823CB").pack(pady=10)
etiqueta4=Label(marco4,text="Desarrollo de Software Multiplataforma",bg="#FA098D").pack(pady=10)


ventana.mainloop()