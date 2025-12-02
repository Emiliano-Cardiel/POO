from tkinter import messagebox
from model import operaciones


class Controladores:
    @staticmethod
    def operaciones(titulo,numero1,numero2,signo):
        if signo=="+":
            resultado=numero1+numero2
        elif signo=="-":
            resultado=numero1-numero2
        elif signo=="x":
            resultado=numero1*numero2
        elif signo=="/":
            resultado=numero1/numero2
        # messagebox.showinfo(icon="info",title=titulo,messsage=f"{numero1}{signo}{numero2}={resultado}")
        respuesta=messagebox.askquestion(title=titulo,message=f"{numero1}{signo}{numero2}={resultado}\n\n¿Quires guardar la operación en la BD?",icon="question")
        if respuesta=="yes":
            operaciones.Operaciones.insertar(numero1,numero2,signo,resultado)
            Controladores.respuesta_sql("Agregar Registro",respuesta)

    @staticmethod
    def eliminar(id):
        respuesta=operaciones.Operaciones.eliminar(id)
        Controladores.respuesta_sql("Borrar Registro",respuesta)

    @staticmethod
    def cambiar(n1,n2,sig,resul,id):
        respuesta=operaciones.Operaciones.actualizar(n1,n2,sig,resul,id)
        Controladores.respuesta_sql("Cambiar Registro",respuesta)

    @staticmethod
    def consultar():
        registros=operaciones.Operaciones.consultar()
        return registros
    
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="... ¡Acción realizada con éxito! ...")
        else:
            messagebox.showerror(icon="warning",title=titulo,message="...No fue posible realizar la acción, vuelva a intentar...")

#controlador=Controladores()
#controlador.operaciones("Sumar",2,3,"+")