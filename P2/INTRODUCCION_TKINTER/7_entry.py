from tkinter import *

# def guardarSaludo():
#     # lbl_result.config(text=f"Hola Bienvenido/a... {txt_nombre.get()} Puta") Otra forma
#     # nombre=txt_nombre.get() Otra Forma
#     lbl_result.config(text=f"Hola Bienvenido/a... {nombre.get()} Puta")
# ventana=Tk()

# ventana.geometry("500x500")
# ventana.title("Entry")

# lbl_name=Label(ventana,text="Ingrese su Nombre:")
# lbl_name.pack()

# nombre=StringVar()
# txt_nombre=Entry(ventana,width=50,textvariable=nombre)
# txt_nombre.pack()

# btn1=Button(ventana,text="Saludar",command=guardarSaludo)
# btn1.pack()

# lbl_result=Label(ventana,text="")
# lbl_result.pack()

# ventana.mainloop()

def inicioSesion():
    lbl_result.config(text=f"Hola Bienvenido/a... {usuario.get()}")

def regresarTexto():
    txt_password.delete(0,END)
    txt_usuario.delete(0,END)
    lbl_result.config(text="")

ventana=Tk()

ventana.title("Entry")
ventana.geometry("800x600")

label_title=Label(ventana,text="Acceso al sistema",)
label_title.config(
    bg="#DED4A3",
    fg="black",
    width=50,
    font="Arial"
)
label_title.pack(pady=15)

label_name=Label(ventana,text="Usuario: ... ")
label_name.pack(pady=10)
usuario=StringVar()
txt_usuario=Entry(ventana,width=50,textvariable=usuario)
txt_usuario.pack()

label_password=Label(ventana,text="Contraseña: ... ")
label_password.pack(pady=10)
password=StringVar()
txt_password=Entry(ventana,width=50,textvariable=password,show="*")
txt_password.pack()

boton_entrar=Button(ventana,text="Entrar",command=inicioSesion).pack(pady=10)
boton_borrar=Button(ventana,text="Borrar",command=regresarTexto).pack(pady=10)

lbl_result=Label(ventana,text="")
lbl_result.pack()

ventana.mainloop()