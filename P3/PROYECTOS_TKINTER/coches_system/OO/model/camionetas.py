from conexionBD import *

class Camionetas:  
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
          cursor.execute(
            "insert into camionetas values(null,%s,%s,%s,%s,%s, %s,%s,%s)",
            (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
          )
          conexion.commit()
          return True
        except:
          return False
    
    @staticmethod
    def consultar():
        try:
          cursor.execute(
            "select * from camionetas"
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id):
       try:
         cursor.execute(
            "update camionetas set marca=%s,color=%s,modelo=%s,velocidad=%s,caballaje=%s,plazas=%s,traccion=%s,cerrada=%s where id=%s",
            (marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
         )
         conexion.commit()
         return True
       except: 
         return False

    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from camionetas where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False

    @staticmethod
    def buscar_camionetas(id):
         try:
              cursor.execute(
                   "select * from camionetas where id=%s",
                   (id,))
              return cursor.fetchone()
         except:
              return []    
        

