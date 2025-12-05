from tkinter import messagebox
from model import autos,camiones,camionetas
        
class Controladores:
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo,message="... ¡Acción realizada con éxito! ...")
        else:
            messagebox.showerror(icon="warning",title=titulo,message="...No fue posible realizar la acción, vuelva a intentar...")

    #Autos
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

    #Camionetas
    @staticmethod
    def insertar_camioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        if cerrada=="Si":
            cerrada=True
        else:
            cerrada=False
        respuesta=camionetas.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
        Controladores.respuesta_sql("Insertar Camioneta",respuesta)

    @staticmethod
    def consultar_camioneta():
        registros=camionetas.Camionetas.consultar()
        return registros
    
    @staticmethod
    def eliminar_camioneta(id):
        respuesta=camionetas.Camionetas.eliminar(id)
        Controladores.respuesta_sql("Borrar Camioneta",respuesta)

    @staticmethod
    def cambiar_camioneta(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
        if cerrada=="Si":
            cerrada=1
        else:
            cerrada=0
        respuesta=camionetas.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
        Controladores.respuesta_sql("Actualizar Camioneta",respuesta)

    #Camiones
    @staticmethod
    def insertar_camion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        respuesta=camiones.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
        Controladores.respuesta_sql("Insertar Camión",respuesta)

    @staticmethod
    def consultar_camion():
        registros=camiones.Camiones.consultar()
        return registros
    
    @staticmethod
    def eliminar_camion(id):
        respuesta=camiones.Camiones.eliminar(id)
        Controladores.respuesta_sql("Borrar Camión",respuesta)

    @staticmethod
    def cambiar_camion(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
        respuesta=camiones.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
        Controladores.respuesta_sql("Actualizar Camión",respuesta)