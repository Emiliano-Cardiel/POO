from tkinter import *
from tkinter import messagebox
from controller import controlador
from model import autos,camionetas,camiones

class Vistas:
    def __init__(self,ventana):
        ventana.title("Gestión de Vehículos")
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

        lbl_titulo=Label(ventana,text=".::Menu Principal::.",justify="center",font=("arial","14"))
        lbl_titulo.pack(pady=10)

        btn_autos=Button(ventana,text="1.- Autos",font=("arial","12"),
                        command=lambda: Vistas.menu_acciones(ventana,"autos"))
        btn_autos.pack(pady=10)
        
        btn_camionetas=Button(ventana,text="2.- Camionetas",font=("arial","12"),
                        command=lambda: Vistas.menu_acciones(ventana,"camionetas"))
        btn_camionetas.pack(pady=10)

        btn_camiones=Button(ventana,text="3.- Camiones",font=("arial","12"),
                        command=lambda: Vistas.menu_acciones(ventana,"camiones"))
        btn_camiones.pack(pady=10)

        btn_salir=Button(ventana,text="4.- Salir",font=("arial","12"),command=ventana.quit)
        btn_salir.pack(pady=10)

    @staticmethod
    def menu_acciones(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        
        if tipo=="autos":
            lbl_titulo=Label(ventana,text=".::Menu De Autos::.",justify="center")
            lbl_titulo.pack(pady=10)
            global tipo1
            tipo1="Autos"
        elif tipo=="camionetas":
            lbl_titulo=Label(ventana,text=".::Menu De Camionetas::.",justify="center")
            lbl_titulo.pack(pady=10)
            global tipo2
            tipo2="Camionetas"
        elif tipo=="camiones":
            lbl_titulo=Label(ventana,text=".::Menu De Camiones::.",justify="center")
            lbl_titulo.pack(pady=10)
            global tipo3
            tipo3="Camiones"

        if tipo=="autos":
            Button(ventana, text="1.- Insertar", command=lambda: Vistas.insertar_autos(ventana)).pack(pady=5)
        elif tipo=="camionetas":
            Button(ventana, text="1.- Insertar", command=lambda: Vistas.insertar_camionetas(ventana)).pack(pady=5)
        elif tipo=="camiones":
            Button(ventana, text="1.- Insertar", command=lambda: Vistas.insertar_camiones(ventana)).pack(pady=5)

        if tipo=="autos":
            Button(ventana, text="2.- Consultar", command=lambda: Vistas.consultar_autos(ventana)).pack(pady=5)
        elif tipo=="camionetas":
            Button(ventana, text="2.- Consultar", command=lambda: Vistas.consultar_camionetas(ventana)).pack(pady=5)
        elif tipo=="camiones":
            Button(ventana, text="2.- Consultar", command=lambda: Vistas.consultar_camiones(ventana)).pack(pady=5)

        if tipo=="autos":
            Button(ventana, text="3.- Actualizar", command=lambda: Vistas.buscar_auto(ventana,"cambiar")).pack(pady=5)
        elif tipo=="camionetas":
            Button(ventana, text="3.- Actualizar", command=lambda: Vistas.buscar_camioneta(ventana,"cambiar")).pack(pady=5)
        elif tipo=="camiones":
            Button(ventana, text="3.- Actualizar", command=lambda: Vistas.buscar_camion(ventana,"cambiar")).pack(pady=5)

        if tipo=="autos":
            Button(ventana, text="4.- Eliminar", command=lambda: Vistas.buscar_auto(ventana,"borrar")).pack(pady=5)
        elif tipo=="camionetas":
            Button(ventana, text="4.- Eliminar", command=lambda: Vistas.buscar_camioneta(ventana,"borrar")).pack(pady=5)
        elif tipo=="camiones":
            Button(ventana, text="4.- Eliminar", command=lambda: Vistas.buscar_camion(ventana,"borrar")).pack(pady=5)

        btn_regresar=Button(ventana,text="5.- Regresar",
                        command=lambda: Vistas.menu_principal(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def insertar_autos(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Ingresa los Datos del Vehículo tipo: {tipo1}::.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca:",justify="center")
        lbl_marca.pack(pady=10)

        marca=StringVar()
        txt_marca=Entry(ventana,width=20,textvariable=marca,justify="left")
        txt_marca.focus()
        txt_marca.pack(side="top",anchor="center")

        lbl_color=Label(ventana,text="Color:",justify="center")
        lbl_color.pack(pady=10)

        color=StringVar()
        txt_color=Entry(ventana,width=20,textvariable=color,justify="left")
        txt_color.pack(side="top",anchor="center")

        lbl_modelo=Label(ventana,text="Modelo:",justify="center")
        lbl_modelo.pack(pady=10)

        modelo=StringVar()
        txt_modelo=Entry(ventana,width=20,textvariable=modelo,justify="left")
        txt_modelo.pack(side="top",anchor="center")

        lbl_velocidad=Label(ventana,text="Velocidad:",justify="center")
        lbl_velocidad.pack(pady=10)

        velocidad=IntVar()
        txt_velocidad=Entry(ventana,width=20,textvariable=velocidad,justify="right")
        txt_velocidad.pack(side="top",anchor="center")

        lbl_potencia=Label(ventana,text="Potencia:",justify="center")
        lbl_potencia.pack(pady=10)

        potencia=IntVar()
        txt_potencia=Entry(ventana,width=20,textvariable=potencia,justify="right")
        txt_potencia.pack(side="top",anchor="center")

        lbl_plazas=Label(ventana,text="Plazas:",justify="center")
        lbl_plazas.pack(pady=10)

        plazas=IntVar()
        txt_plazas=Entry(ventana,width=20,textvariable=plazas,justify="right")
        txt_plazas.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: controlador.Controladores.insertar_auto(marca.get(),color.get(),modelo.get(),velocidad.get(),potencia.get(),plazas.get()))
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"autos"))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f"Los vehículos de tipo: {tipo1}, son:",justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=controlador.Controladores.consultar_auto()
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"\nAuto: {num_notas} \tID:{fila[0]}\n\tMarca:{fila[1]}\t Color: {fila[2]}\t Modelo: {fila[3]}\tVelocidad: {fila[4]}\t Potencia: {fila[5]}\t Plazas: {fila[6]}" 
                num_notas+=1
        else:
            messagebox.showwarning(icon="warning",message="...:: No existen notas para este usuario ::..")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana,text="Volver",justify="center",
                        command=lambda: Vistas.menu_acciones(ventana,"autos"))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_autos(ventana,id_):
        registro=autos.Autos.buscar_autos(id_)
        if registro is None:
            messagebox.showwarning(icon="warning",message="... El Automóvil no se encuentra disponible en la BD ...")
        else:
            Vistas.borrarPantalla(ventana)

            lbl_titulo=Label(ventana,text=f".::Ingresa los Datos Nuevos del Vehículo tipo: {tipo1}::.",justify="center")
            lbl_titulo.pack(pady=10)

            lbl_id=Label(ventana,text="ID del Vehículo a modificar:",justify="center")
            lbl_id.pack(pady=10)

            id=IntVar()
            txt_id=Entry(ventana,width=20,textvariable=id,justify="right",state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(side="top",anchor="center")

            lbl_marca_new=Label(ventana,text="Nueva Marca:",justify="center")
            lbl_marca_new.pack(pady=10)

            marca=StringVar()
            txt_marca_new=Entry(ventana,width=20,textvariable=marca,justify="left")
            marca.set(registro[1])
            txt_marca_new.pack(side="top",anchor="center")

            lbl_color_new=Label(ventana,text="Nuevo Color:",justify="center")
            lbl_color_new.pack(pady=10)

            color=StringVar()
            txt_color_new=Entry(ventana,width=20,textvariable=color,justify="left")
            color.set(registro[2])
            txt_color_new.pack(side="top",anchor="center")

            lbl_modelo_new=Label(ventana,text="Nuevo Modelo:",justify="center")
            lbl_modelo_new.pack(pady=10)

            modelo=StringVar()
            txt_modelo_new=Entry(ventana,width=20,textvariable=modelo,justify="left")
            modelo.set(registro[3])
            txt_modelo_new.pack(side="top",anchor="center")

            lbl_velocidad_new=Label(ventana,text="Nueva Velocidad:",justify="center")
            lbl_velocidad_new.pack(pady=10)

            velocidad=IntVar()
            txt_velocidad_new=Entry(ventana,width=20,textvariable=velocidad,justify="right")
            velocidad.set(registro[4])
            txt_velocidad_new.pack(side="top",anchor="center")

            lbl_potencia_new=Label(ventana,text="Nueva Potencia:",justify="center")
            lbl_potencia_new.pack(pady=10)

            potencia=IntVar()
            txt_potencia_new=Entry(ventana,width=20,textvariable=potencia,justify="right")
            potencia.set(registro[5])
            txt_potencia_new.pack(side="top",anchor="center")

            lbl_plazas_new=Label(ventana,text="Nuevas Plazas:",justify="center")
            lbl_plazas_new.pack(pady=10)

            plazas=IntVar()
            txt_plazas_new=Entry(ventana,width=20,textvariable=plazas,justify="right")
            plazas.set(registro[6])
            txt_plazas_new.pack(side="top",anchor="center")

            btn_guardar=Button(ventana,text="Guardar",
                            command=lambda: controlador.Controladores.cambiar_auto(marca.get(),color.get(),modelo.get(),velocidad.get(),potencia.get(),plazas.get(),id.get()))
            btn_guardar.pack(pady=10)
            
            btn_volver=Button(ventana,text="Volver",
                            command=lambda: Vistas.menu_acciones(ventana,"autos"))
            btn_volver.pack(pady=10)

    @staticmethod
    def borrar_autos(ventana,id_):
        registro=autos.Autos.buscar_autos(id_)
        if registro is None:
            messagebox.showwarning(icon="warning",message="... El Automóvil no se encuentra disponible en la BD ...")
        else:
            Vistas.borrarPantalla(ventana)
            lbl_titulo0=Label(ventana,text=f".:: Eliminación de Vehículos de tipo: {tipo1}::.",justify="center")
            lbl_titulo0.pack(pady=10)

            lbl_id=Label(ventana,text="ID del Vehiculo a Eliminar:",justify="center")
            lbl_id.pack(pady=10)

            id=IntVar()
            txt_id=Entry(ventana,justify="left",textvariable=id,state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(side="top",anchor="center")

            btn_eliminar=Button(ventana,text="Eliminar",
                            command=lambda: controlador.Controladores.eliminar_auto(id_))
            btn_eliminar.pack(pady=10)
            
            btn_volver=Button(ventana,text="Volver",
                            command=lambda: Vistas.menu_acciones(ventana,"autos"))
            btn_volver.pack(pady=10)

    @staticmethod
    def insertar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Ingresa los Datos del Vehículo tipo: {tipo2}::.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca:",justify="center")
        lbl_marca.pack(pady=10)

        txt_marca=Entry(ventana,width=20,justify="left")
        txt_marca.focus()
        txt_marca.pack(side="top",anchor="center")

        lbl_color=Label(ventana,text="Color:",justify="center")
        lbl_color.pack(pady=10)

        txt_color=Entry(ventana,width=20,justify="left")
        txt_color.pack(side="top",anchor="center")

        lbl_modelo=Label(ventana,text="Modelo:",justify="center")
        lbl_modelo.pack(pady=10)

        txt_modelo=Entry(ventana,width=20,justify="left")
        txt_modelo.pack(side="top",anchor="center")

        lbl_velocidad=Label(ventana,text="Velocidad:",justify="center")
        lbl_velocidad.pack(pady=10)

        txt_velocidad=Entry(ventana,width=20,justify="left")
        txt_velocidad.pack(side="top",anchor="center")

        lbl_potencia=Label(ventana,text="Potencia:",justify="center")
        lbl_potencia.pack(pady=10)

        txt_potencia=Entry(ventana,width=20,justify="left")
        txt_potencia.pack(side="top",anchor="center")

        lbl_plazas=Label(ventana,text="Plazas:",justify="center")
        lbl_plazas.pack(pady=10)

        txt_plazas=Entry(ventana,width=20,justify="left")
        txt_plazas.pack(side="top",anchor="center")

        lbl_traccion=Label(ventana,text="Tracción:",justify="center")
        lbl_traccion.pack(pady=10)

        txt_traccion=Entry(ventana,width=20,justify="left")
        txt_traccion.pack(side="top",anchor="center")

        lbl_cerrada=Label(ventana,text="Caja Cerrada S/N:",justify="center")
        lbl_cerrada.pack(pady=10)

        txt_cerrada=Entry(ventana,width=20,justify="left")
        txt_cerrada.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: "")
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"camionetas"))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f"Los vehículos de tipo: {tipo2}, son:",justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=[["BMW","Rojo","2020","300km/h","400","4",]]
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"\nCamionetas: {num_notas}\n\tMarca:{fila[0]}\t Color: {fila[1]}\t Modelo: {fila[2]}\tVelocidad: {fila[3]}\t Potencia: {fila[4]}\t Plazas: {fila[5]}" 
                num_notas+=1
        else:
            messagebox.showwarning(icon="warning",message="...:: No existen notas para este usuario ::..")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana,text="Volver",justify="center",
                        command=lambda: Vistas.menu_acciones(ventana,"camionetas"))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Ingresa los Datos Nuevos del Vehículo tipo: {tipo2}::.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID del Vehículo a modificar:",justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana,width=20,justify="left")
        txt_id.focus()
        txt_id.pack(side="top",anchor="center")

        lbl_marca_new=Label(ventana,text="Nueva Marca:",justify="center")
        lbl_marca_new.pack(pady=10)

        txt_marca_new=Entry(ventana,width=20,justify="left")
        txt_marca_new.pack(side="top",anchor="center")

        lbl_color_new=Label(ventana,text="Nuevo Color:",justify="center")
        lbl_color_new.pack(pady=10)

        txt_color_new=Entry(ventana,width=20,justify="left")
        txt_color_new.pack(side="top",anchor="center")

        lbl_modelo_new=Label(ventana,text="Nuevo Modelo:",justify="center")
        lbl_modelo_new.pack(pady=10)

        txt_modelo_new=Entry(ventana,width=20,justify="left")
        txt_modelo_new.pack(side="top",anchor="center")

        lbl_velocidad_new=Label(ventana,text="Nueva Velocidad:",justify="center")
        lbl_velocidad_new.pack(pady=10)

        txt_velocidad_new=Entry(ventana,width=20,justify="left")
        txt_velocidad_new.pack(side="top",anchor="center")

        lbl_potencia_new=Label(ventana,text="Nueva Potencia:",justify="center")
        lbl_potencia_new.pack(pady=10)

        txt_potencia_new=Entry(ventana,width=20,justify="left")
        txt_potencia_new.pack(side="top",anchor="center")

        lbl_plazas_new=Label(ventana,text="Nuevas Plazas:",justify="center")
        lbl_plazas_new.pack(pady=10)

        txt_plazas_new=Entry(ventana,width=20,justify="left")
        txt_plazas_new.pack(side="top",anchor="center")

        lbl_traccion_new=Label(ventana,text="Nueva Tracción:",justify="center")
        lbl_traccion_new.pack(pady=10)

        txt_traccion_new=Entry(ventana,width=20,justify="left")
        txt_traccion_new.pack(side="top",anchor="center")

        lbl_cerrada_new=Label(ventana,text="Nueva Caja Cerrada S/N:",justify="center")
        lbl_cerrada_new.pack(pady=10)

        txt_cerrada_new=Entry(ventana,width=20,justify="left")
        txt_cerrada_new.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: "")
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"camionetas"))
        btn_volver.pack(pady=10)

    @staticmethod
    def borrar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo0=Label(ventana,text=f".:: Eliminación de Vehículos de tipo: {tipo2}::.",justify="center")
        lbl_titulo0.pack(pady=10)

        lbl_id=Label(ventana,text="ID del Vehiculo a Eliminar:",justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana,justify="left")
        txt_id.focus()
        txt_id.pack(side="top",anchor="center")

        btn_eliminar=Button(ventana,text="Eliminar",
                        command=lambda: "")
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"camionetas"))
        btn_volver.pack(pady=10)

    @staticmethod
    def insertar_camiones(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Ingresa los Datos del Vehículo tipo: {tipo3}::.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca:",justify="center")
        lbl_marca.pack(pady=10)

        txt_marca=Entry(ventana,width=20,justify="left")
        txt_marca.focus()
        txt_marca.pack(side="top",anchor="center")

        lbl_color=Label(ventana,text="Color:",justify="center")
        lbl_color.pack(pady=10)

        txt_color=Entry(ventana,width=20,justify="left")
        txt_color.pack(side="top",anchor="center")

        lbl_modelo=Label(ventana,text="Modelo:",justify="center")
        lbl_modelo.pack(pady=10)

        txt_modelo=Entry(ventana,width=20,justify="left")
        txt_modelo.pack(side="top",anchor="center")

        lbl_velocidad=Label(ventana,text="Velocidad:",justify="center")
        lbl_velocidad.pack(pady=10)

        txt_velocidad=Entry(ventana,width=20,justify="left")
        txt_velocidad.pack(side="top",anchor="center")

        lbl_potencia=Label(ventana,text="Potencia:",justify="center")
        lbl_potencia.pack(pady=10)

        txt_potencia=Entry(ventana,width=20,justify="left")
        txt_potencia.pack(side="top",anchor="center")

        lbl_plazas=Label(ventana,text="Plazas:",justify="center")
        lbl_plazas.pack(pady=10)

        txt_plazas=Entry(ventana,width=20,justify="left")
        txt_plazas.pack(side="top",anchor="center")

        lbl_eje=Label(ventana,text="Cantidad de Ejes:",justify="center")
        lbl_eje.pack(pady=10)

        txt_eje=Entry(ventana,width=20,justify="left")
        txt_eje.pack(side="top",anchor="center")

        lbl_capacidad_carga=Label(ventana,text="Capacidad de Carga:",justify="center")
        lbl_capacidad_carga.pack(pady=10)

        txt_capacidad_carga=Entry(ventana,width=20,justify="left")
        txt_capacidad_carga.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: "")
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"camiones"))
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_camiones(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f"Los vehículos de tipo: {tipo3}, son:",justify="center")
        lbl_titulo.pack(pady=10)

        filas=""
        registros=[["BMW","Rojo","2020","300km/h","400","4",]]
        if len(registros)>0:
            num_notas=1
            for fila in registros:
                filas=filas+f"\nCamiones: {num_notas}\n\tMarca:{fila[0]}\t Color: {fila[1]}\t Modelo: {fila[2]}\tVelocidad: {fila[3]}\t Potencia: {fila[4]}\t Plazas: {fila[5]}" 
                num_notas+=1
        else:
            messagebox.showwarning(icon="warning",message="...:: No existen notas para este usuario ::..")

        lbl_resultado=Label(ventana,text=f"{filas}")
        lbl_resultado.pack(pady=10)

        btn_volver=Button(ventana,text="Volver",justify="center",
                        command=lambda: Vistas.menu_acciones(ventana,"camiones"))
        btn_volver.pack(pady=10)

    @staticmethod
    def cambiar_camiones(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo=Label(ventana,text=f".::Ingresa los Datos Nuevos del Vehículo tipo: {tipo3}::.",justify="center")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="ID del Vehículo a modificar:",justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana,width=20,justify="left")
        txt_id.focus()
        txt_id.pack(side="top",anchor="center")

        lbl_marca_new=Label(ventana,text="Nueva Marca:",justify="center")
        lbl_marca_new.pack(pady=10)

        txt_marca_new=Entry(ventana,width=20,justify="left")
        txt_marca_new.pack(side="top",anchor="center")

        lbl_color_new=Label(ventana,text="Nuevo Color:",justify="center")
        lbl_color_new.pack(pady=10)

        txt_color_new=Entry(ventana,width=20,justify="left")
        txt_color_new.pack(side="top",anchor="center")

        lbl_modelo_new=Label(ventana,text="Nuevo Modelo:",justify="center")
        lbl_modelo_new.pack(pady=10)

        txt_modelo_new=Entry(ventana,width=20,justify="left")
        txt_modelo_new.pack(side="top",anchor="center")

        lbl_velocidad_new=Label(ventana,text="Nueva Velocidad:",justify="center")
        lbl_velocidad_new.pack(pady=10)

        txt_velocidad_new=Entry(ventana,width=20,justify="left")
        txt_velocidad_new.pack(side="top",anchor="center")

        lbl_potencia_new=Label(ventana,text="Nueva Potencia:",justify="center")
        lbl_potencia_new.pack(pady=10)

        txt_potencia_new=Entry(ventana,width=20,justify="left")
        txt_potencia_new.pack(side="top",anchor="center")

        lbl_plazas_new=Label(ventana,text="Nuevas Plazas:",justify="center")
        lbl_plazas_new.pack(pady=10)

        txt_plazas_new=Entry(ventana,width=20,justify="left")
        txt_plazas_new.pack(side="top",anchor="center")

        lbl_eje_new=Label(ventana,text="Nueva Cantidad de Ejes:",justify="center")
        lbl_eje_new.pack(pady=10)

        txt_eje_new=Entry(ventana,width=20,justify="left")
        txt_eje_new.pack(side="top",anchor="center")

        lbl_capacidad_carga_new=Label(ventana,text="Nueva Capacidad de Carga:",justify="center")
        lbl_capacidad_carga_new.pack(pady=10)

        txt_capacidad_carga_new=Entry(ventana,width=20,justify="left")
        txt_capacidad_carga_new.pack(side="top",anchor="center")

        btn_guardar=Button(ventana,text="Guardar",
                        command=lambda: "")
        btn_guardar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"camiones"))
        btn_volver.pack(pady=10)

    @staticmethod
    def borrar_camiones(ventana):
        Vistas.borrarPantalla(ventana)

        lbl_titulo0=Label(ventana,text=f".:: Eliminación de Vehículos de tipo: {tipo3}::.",justify="center")
        lbl_titulo0.pack(pady=10)

        lbl_id=Label(ventana,text="ID del Vehiculo a Eliminar:",justify="center")
        lbl_id.pack(pady=10)

        txt_id=Entry(ventana,justify="left")
        txt_id.focus()
        txt_id.pack(side="top",anchor="center")

        btn_eliminar=Button(ventana,text="Eliminar",
                        command=lambda: "")
        btn_eliminar.pack(pady=10)
        
        btn_volver=Button(ventana,text="Volver",
                        command=lambda: Vistas.menu_acciones(ventana,"camiones"))
        btn_volver.pack(pady=10)

    @staticmethod
    def buscar_auto(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Buscar una Operacion para: Autos ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="\nID del Auto a Buscar:")
        lbl_id.pack(pady=5)
        
        id=IntVar()
        txt_id=Entry(ventana,width=10,textvariable=id,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana, text="Buscar", command=lambda: Vistas.cambiar_autos(ventana,id.get())).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana, text="Buscar", command=lambda: Vistas.borrar_autos(ventana,id.get())).pack(pady=5)

        btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana,"autos"))
        btn_volver.pack(pady=5)

    @staticmethod
    def buscar_camioneta(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Buscar una Operacion para: Camionetas ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="\nID de la Camioneta a Buscar:")
        lbl_id.pack(pady=5)
        
        id=IntVar()
        txt_id=Entry(ventana,width=10,textvariable=id,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana, text="Buscar", command=lambda: Vistas.cambiar_camionetas(ventana,id.get())).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana, text="Buscar", command=lambda: Vistas.borrar_camionetas(ventana,id.get())).pack(pady=5)

        btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana,"camioneta"))
        btn_volver.pack(pady=5)

    @staticmethod
    def buscar_camion(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=".:: Buscar una Operacion para: Camion ::.")
        lbl_titulo.pack(pady=10)

        lbl_id=Label(ventana,text="\nID del Camion a Buscar:")
        lbl_id.pack(pady=5)
        
        id=IntVar()
        txt_id=Entry(ventana,width=10,textvariable=id,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana, text="Buscar", command=lambda: Vistas.cambiar_camiones(ventana,id.get())).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana, text="Buscar", command=lambda: Vistas.borrar_camiones(ventana,id.get())).pack(pady=5)

        btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana,"camiones"))
        btn_volver.pack(pady=5)