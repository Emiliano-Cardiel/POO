from tkinter import messagebox
from model import usuario,nota
from view import vista

class Controlador:
    #Usuarios
    @staticmethod
    def registrar(nombre,apellidos,email,password):
        resultado=usuario.Usuario.registrar(nombre,apellidos,email,password)
        if resultado:
            messagebox.showinfo(icon="info",message=f"{nombre} {apellidos}, se registro correctamente, con el email: {email}")
        else:
            messagebox.showwarning(icon="warning",message="** Porfvor intentalo nuevamente, no fue posible registrar el usuario **")

    @staticmethod
    def login(email,password,ventana):
        registro=usuario.Usuario.iniciar_sesion(email,password)
        if registro:
            messagebox.showinfo(icon="info",message=f"{registro[1]} {registro[2]}, haz iniciado sesión correctamente")
            vista.Vistas.menu_notas(ventana,registro[0],registro[1],registro[2])
        else:
            messagebox.showwarning(icon="warning",message="** Porfvor intentalo nuevamente, Credenciales incorrectas **")
    #Notas
    @staticmethod
    def crear(usuario_id,titulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear Notas",respuesta)

    @staticmethod
    def mostrar(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros
    
    @staticmethod
    def eliminar(id):
        respuesta=nota.Nota.eliminar(id)
        Controlador.respuesta_sql("Eliminar Notas",respuesta)

    @staticmethod
    def modificar(id,titulo,descripcion):
        respuesta=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.respuesta_sql("Nota a Modificar",respuesta)

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="... ¡Acción realizada con éxito! ...")
        else:
            messagebox.showerror(icon="warning",title=titulo,message="...No fue posible realizar la acción, vuelva a intentar...")


        
   
    