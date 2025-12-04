from tkinter import messagebox
from model import autos,camiones,camionetas
        
class Controladores:
    #Autos
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="... ¡Acción realizada con éxito! ...")
        else:
            messagebox.showerror(icon="warning",title=titulo,message="...No fue posible realizar la acción, vuelva a intentar...")

    @staticmethod
    def insertar_auto(marca,color,modelo,velocidad,caballaje,plazas):
        respuesta=autos.Autos.insertar(marca,color,modelo,velocidad,caballaje,plazas)
        Controladores.respuesta_sql("Insertar Auto",respuesta)

    @staticmethod
    def consultar_auto():
        registros=autos.Autos.consultar()
        return registros
    
    @staticmethod
    def eliminar_auto(id):
        respuesta=autos.Autos.eliminar(id)
        Controladores.respuesta_sql("Borrar Auto",respuesta)

    @staticmethod
    def cambiar_auto(marca,color,modelo,velocidad,caballaje,plazas,id):
        respuesta=autos.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
        Controladores.respuesta_sql("Actualizar Auto",respuesta)