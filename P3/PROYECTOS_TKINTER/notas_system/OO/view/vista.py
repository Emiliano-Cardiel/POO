from tkinter import *
from tkinter import messagebox
from controller import controlador

class Vistas:
    def __init__(self,ventana):
        ventana.title("Gestión de Notas")
        ventana.geometry("1024x768")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_registro=Label(ventana,text=".::Menu Principal::.",justify="center")
        lbl_registro.pack(pady=10)

        btn_registro=Button(ventana,text="1.- Registro",
                        command=lambda: Vistas.registro(ventana))
        btn_registro.pack(pady=10)
        
        btn_login=Button(ventana,text="2.- Login",
                        command=lambda: Vistas.inicio_sesion(ventana))
        btn_login.pack(pady=10)

        btn_salir=Button(ventana,text="3.- Salir",command=ventana.quit)
        btn_salir.pack(pady=10)

    @staticmethod
    def registro(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_inicio=Label(ventana,text=".::Registro en el Sistema::.",justify="center")
        lbl_inicio.pack(pady=10)

        lbl_nombre=Label(ventana,text="¿Cúal es tu nombre?",justify="center")
        lbl_nombre.pack(pady=10)

        txt_nombre=Entry(ventana,width=25,justify="left")
        txt_nombre.focus()
        txt_nombre.pack(side="top",anchor="center")

        lbl_apellidos=Label(ventana,text="¿Cúales son tus apellidos?",justify="center")
        lbl_apellidos.pack(pady=10)

        txt_apellidos=Entry(ventana,width=25,justify="left")
        txt_apellidos.pack(side="top",anchor="center")

        lbl_email=Label(ventana,text="Ingresa tu email:",justify="center")
        lbl_email.pack(pady=10)

        txt_email=Entry(ventana,width=25,justify="left")
        txt_email.pack(side="top",anchor="center")

        lbl_password=Label(ventana,text="Ingresa tu contraseña:",justify="center")
        lbl_password.pack(pady=10)

        txt_password=Entry(ventana,width=25,justify="left",show="*")
        txt_password.pack(side="top",anchor="center")

        btn_registrar=Button(ventana,text="Registrar",
                        command=lambda: {controlador.Controlador.registrar(txt_nombre.get(),txt_apellidos.get(),txt_email.get(),txt_password.get()), Vistas.inicio_sesion(ventana)})
        btn_registrar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def inicio_sesion(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_inicio=Label(ventana,text=".::Inicio de Sesión::.",justify="center")
        lbl_inicio.pack(pady=10)

        lbl_email=Label(ventana,text="Ingresa tu email:",justify="center")
        lbl_email.pack(pady=10)

        txt_email=Entry(ventana,width=30,justify="left")
        txt_email.pack(side="top",anchor="center")

        lbl_password=Label(ventana,text="Ingresa tu contraseña:",justify="center")
        lbl_password.pack(pady=10)

        txt_password=Entry(ventana,width=30,justify="left",show="*")
        txt_password.pack(side="top",anchor="center")

        btn_registrar=Button(ventana,text="Entrar",
                        command=lambda: controlador.Controlador.login(txt_email.get(),txt_password.get(),ventana))
        btn_registrar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def menu_notas(ventana,usuario_id,nombre,apellidos):
        Vistas.borrarPantalla(ventana)

        global id_user,nom_user,ape_user
        id_user=usuario_id
        nom_user=nombre
        ape_user=apellidos

        lbl_registro=Label(ventana,text=f".::Bienvenido {nombre} {apellidos}, has iniciado sesión::.",justify="center")
        lbl_registro.pack(pady=10)

        btn_crear=Button(ventana,text="1.- Crear",
                        command=lambda: Vistas.crear_nota(ventana))
        btn_crear.pack(pady=10)
        
        btn_mostrar=Button(ventana,text="2.- Mostrar",
                        command=lambda: Vistas.mostrar_notas(ventana))
        btn_mostrar.pack(pady=10)

        btn_cambiar=Button(ventana,text="3.- Cambiar",
                        command=lambda: Vistas.modificar_nota(ventana))
        btn_cambiar.pack(pady=10)

        btn_eliminar=Button(ventana,text="4.- Eliminar",
                        command=lambda: Vistas.eliminar_nota(ventana))
        btn_eliminar.pack(pady=10)
        
        btn_regresar=Button(ventana,text="5.- Regresar",
                        command=lambda: Vistas.inicio_sesion(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def crear_nota(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_nota=Label(ventana,text=".::Crear Nota::.",justify="center")
        lbl_nota.pack(pady=10)

        lbl_titulo=Label(ventana,text="Título:",justify="center")
        lbl_titulo.pack(pady=10)

        txt_titulo=Entry(ventana,width=20,justify="left")
        txt_titulo.focus()
        txt_titulo.pack(side="top",anchor="center")

        lbl_descripcion=Label(ventana,text="Descripción:",justify="center")
        lbl_descripcion.pack(pady=10)

        txt_descripcion=Entry(ventana,width=20,justify="left")
        txt_descripcion.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: controlador.Controlador.crear(id_user,txt_titulo.get(),txt_descripcion.get()))
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def mostrar_notas(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f"{nom_user} {ape_user}, tus notas son:",justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=controlador.Controlador.mostrar(id_user)
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"\nNota: {num_notas}\nID:{fila[0]}.- Título: {fila[2]} Fecha de Creación: {fila[4]}\n Descripción: {fila[3]}" 
                num_notas+=1
        else:
            messagebox.showwarning(icon="warning",message="...:: No existen notas para este usuario ::..")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana,text="Volver",justify="center",
                        command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def modificar_nota(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo0=Label(ventana,text=f".:: {nom_user} {ape_user}, vamos a modificar una Nota ::.",justify="center")
        lbl_titulo0.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la Nota a Cambiar:",justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana,justify="left")
        txt_id.focus()
        txt_id.pack(side="top",anchor="center")

        lbl_nuevo_titulo=Label(ventana,text="Nuevo Título:",justify="center")
        lbl_nuevo_titulo.pack(pady=10)

        txt_nuevo_titulo=Entry(ventana,justify="left")
        txt_nuevo_titulo.pack(side="top",anchor="center")

        lbl_nueva_descripcion=Label(ventana,text="Nueva Descripción:",justify="center")
        lbl_nueva_descripcion.pack(pady=10)

        txt_nueva_descripcion=Entry(ventana,justify="left")
        txt_nueva_descripcion.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: controlador.Controlador.modificar(txt_id.get(),txt_nuevo_titulo.get(),txt_nueva_descripcion.get()))
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def eliminar_nota(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo0=Label(ventana,text=f".:: {nom_user} {ape_user}, vamos a eliminar una Nota ::.",justify="center")
        lbl_titulo0.pack(pady=10)

        lbl_id=Label(ventana,text="ID de la Nota a Eliminar:",justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana,justify="left")
        txt_id.focus()
        txt_id.pack(side="top",anchor="center")

        btn_eliminar=Button(ventana,text="Eliminar",
                        command=lambda: controlador.Controlador.eliminar(txt_id.get()))
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_notas(ventana,id_user,nom_user,ape_user))
        btn_volver.pack(pady=10)
