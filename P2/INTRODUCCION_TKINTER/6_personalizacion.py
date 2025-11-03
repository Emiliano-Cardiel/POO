from tkinter import *

def cambiarEtiqueta():
    main_label.config(text="POO con Python")
    main_label.config(
        bg="darkgreen",
        fg="white",
        cursor="spider"
    )

def regresarEtiqueta():
    main_label.config(text="Bienvenidos a Tkinter")
    main_label.config(
        bg="lightblue",
        fg="darkblue",
        cursor="spider"
    )

ventana=Tk()

ventana.title("Personalizar Widgets u Objetos")
ventana.geometry("500x500")

main_label=Label(ventana,text="Bienvenidos a Tkinter")
main_label.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetical",30,"italic"),
    relief=SOLID,
    border=2
)
main_label.pack(pady=25)

boton1=Button(ventana,text="Haz Clic ...",command=cambiarEtiqueta)
boton1.config(
    bg="blue",
    fg="white",
    width=15,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="yellow",
    activebackground="red", 
)
boton1.pack(pady=15)

boton2=Button(ventana,text="Regresar Valores",command=regresarEtiqueta)
boton2.config(
    bg="blue",
    fg="white",
    width=15,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="yellow",
    activebackground="red",
)
boton2.pack(pady=15)

ventana.mainloop()