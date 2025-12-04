from conexionBD import *

class Camiones:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        try:
          cursor.execute(
            "insert into camiones values(null,%s,%s,%s,%s,%s, %s,%s,%s)",
            (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
          )
          conexion.commit()
          return True
        except:
          return False
    
    @staticmethod
    def consultar():
        try:
          cursor.execute(
            "select * from camiones"
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id):
       try:
         cursor.execute(
            "update camiones set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,eje=%s,capacidadCarga=%s where id=%s",
            (marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
         )
         conexion.commit()
         return True
       except: 
         return False

    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from camiones where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False

    @staticmethod
    def buscar_camiones(id):
         try:
              cursor.execute(
                   "select * from camiones where id=%s",
                   (id,))
              return cursor.fetchone()
         except:
              return []    