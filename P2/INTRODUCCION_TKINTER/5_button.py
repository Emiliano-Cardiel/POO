from tkinter import *

def cambiarTexto():
    label_name.config(text="Emiliano Arturo Cardiel Mares")
    label_password.config(text="1234")

def regresarTexto():
    label_name.config(text="Usuario: ...")
    label_password.config(text="Contraseña: ...")

ventana=Tk()

ventana.title("Uso de Botones, Marcos, Etiquetas")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    width=800,
    height=100,bg="silver",
    border=2,
    relief=SOLID
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_title=Label(frame_principal,text="Inicio de Sesión",)
label_title.config(
    bg="silver",
    height=50,
    font="Arial"
)
label_title.pack(pady=30)

label_name=Label(ventana,text="Usuario: ... ")
label_name.pack(pady=10)
label_password=Label(ventana,text="Contraseña: ... ")
label_password.pack(pady=10)

boton_aceptar=Button(ventana,text="Entrar",command=cambiarTexto).pack(pady=10)
boton_regresar=Button(ventana,text="Regresar",command=regresarTexto).pack(pady=10)

ventana.mainloop()