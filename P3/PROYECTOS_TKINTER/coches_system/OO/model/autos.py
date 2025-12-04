from conexionBD import *

class Autos:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas):
        try:
          cursor.execute(
            "insert into autos values(null,%s,%s,%s,%s,%s, %s)",
            (marca,color,modelo,velocidad,caballaje,plazas)
          )
          conexion.commit()
          return True
        except:
          return False
       
    @staticmethod
    def consultar():
        try:
          cursor.execute(
            "select * from autos"
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(marca, color, modelo,velocidad,caballaje,plazas,id):
       try:
         cursor.execute(
            "update autos set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s where id=%s",
            (marca, color, modelo,velocidad,caballaje,plazas,id)
         )
         conexion.commit()
         return True
       except: 
         return False

    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from autos where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False

    @staticmethod
    def buscar_autos(id):
         try:
              cursor.execute(
                   "select * from autos where id=%s",
                   (id,))
              return cursor.fetchone()
         except:
              return []    
