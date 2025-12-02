from tkinter import *
from controller import funciones
from model import operaciones
from tkinter import messagebox

#Interfaz o View:
class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora Básica")
        ventana.geometry("1024x768")
        ventana.resizable(False,False)
        self.interfaz(ventana)

    @staticmethod
    def interfaz(ventana):
        Vistas.borrarPantalla(ventana)
        Vistas.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()

        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        txt_numero1.focus()
        txt_numero1.pack(side="top",anchor="center")

        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        txt_numero2.pack(side="top",anchor="center")

        btn_suma=Button(ventana,text="SUMAR +",
                        command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_suma.pack()
        
        btn_resta=Button(ventana,text="RESTAR -",
                        command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="MULTIPLICAR x",
                        command=lambda: funciones.Controladores.operaciones("Multiplicación",n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()

        btn_division=Button(ventana,text="DIVIDIR /",
                        command=lambda: funciones.Controladores.operaciones("División",n1.get(),n2.get(),"/"))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack()

    @staticmethod
    def menuPrincipal(ventana):
        Vistas.borrarPantalla(ventana)
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)

        operaMenu=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=operaMenu)
        operaMenu.add_command(label="Agregar", command=lambda: Vistas.interfaz(ventana))
        operaMenu.add_command(label="Consultar", command=lambda: Vistas.consultar(ventana))
        operaMenu.add_command(label="Cambiar", command=lambda: Vistas.buscar(ventana,"cambiar"))
        operaMenu.add_command(label="Borrar", command=lambda: Vistas.buscar(ventana,"borrar"))
        operaMenu.add_separator()
        operaMenu.add_command(label="Salir",command=ventana.quit)

    @staticmethod
    def eliminar(ventana,id_):
        registro=operaciones.Operaciones.buscar(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="... La operación no se encuentra disponible en la BD ...")
        else:
            Vistas.borrarPantalla(ventana)
            Vistas.menuPrincipal(ventana)
            lbl1=Label(ventana,text=".:: Borrar una Operacion ::.")
            lbl1.pack(pady=10)

            lbl2=Label(ventana,text="\nID de la Operación:")
            lbl2.pack(pady=5)
            
            id=IntVar()
            txt_id=Entry(ventana,width=10,textvariable=id,justify="right",state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            btn_eliminar=Button(ventana, text="Eliminar", command=lambda: funciones.Controladores.eliminar(id_))
            btn_eliminar.pack(pady=5)

            btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.interfaz(ventana))
            btn_volver.pack(pady=5)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def consultar(ventana):
        Vistas.menuPrincipal(ventana)
        lbl1=Label(ventana,text=".:: Listado de las Operaciones ::.")
        lbl1.pack(pady=10)

        registros=funciones.Controladores.consultar()
        filas=""
        if len(registros)>0:
            num_operaciones=1
            for fila in registros:
                filas=filas+f"\nOperacion: {num_operaciones} ID:{fila[0]} Fecha de Creación: {fila[1]} \nOperacion: {fila[2]}{fila[4]}{fila[3]}={fila[5]}"
                num_operaciones+=1
        else:
            messagebox.showerror(icon="warning",title=".::Alerta::.",message=".. No hay datos en el sistema .. Agrega más Operaciones")

        lbl2=Label(ventana, text=f"{filas}")
        lbl2.pack(pady=10)

        btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.interfaz(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def buscar(ventana,tipo):
        Vistas.borrarPantalla(ventana)
        Vistas.menuPrincipal(ventana)
        lbl1=Label(ventana,text=".:: Buscar una Operacion ::.")
        lbl1.pack(pady=10)

        lbl2=Label(ventana,text="\nID de la Operación a Buscar:")
        lbl2.pack(pady=5)
        
        id=IntVar()
        txt_id=Entry(ventana,width=10,textvariable=id,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana, text="Buscar", command=lambda: Vistas.cambiar_id(ventana,id.get())).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana, text="Buscar", command=lambda: Vistas.eliminar(ventana,id.get())).pack(pady=5)

        btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.interfaz(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def cambiar_id(ventana,id_):
        registro=operaciones.Operaciones.buscar(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="... La operación no se encuentra disponible en la BD ...")
        else:
            Vistas.borrarPantalla(ventana)
            Vistas.menuPrincipal(ventana)

            lbl_titulo=Label(ventana,text=".:: Cambiar una Operación ::.")
            lbl_titulo.pack(pady=10)

            id=IntVar()
            txt_id=Entry(ventana,width=10,textvariable=id,justify="right",state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)

            lbl_num1=Label(ventana,text="Nuevo Número 1:")
            lbl_num1.pack(pady=5)
            num1=IntVar()
            txt_num1=Entry(ventana,width=10,textvariable=num1,justify="right")
            num1.set(registro[2])
            txt_num1.pack(pady=5)
                    
            lbl_num2=Label(ventana,text="Nuevo Número 2:")
            lbl_num2.pack(pady=5)
            num2=IntVar()
            txt_num2=Entry(ventana,width=10,textvariable=num2,justify="right")
            num2.set(registro[3])
            txt_num2.pack(pady=5)

            lbl_signo=Label(ventana,text="Nuevo Signo:")
            lbl_signo.pack(pady=5)
            signo=StringVar()
            txt_signo=Entry(ventana,width=10,textvariable=signo,justify="center")
            signo.set(registro[4])
            txt_signo.pack(pady=5)

            lbl_result=Label(ventana,text="Nuevo Resultado:")
            lbl_result.pack(pady=5)
            result=IntVar()
            txt_result=Entry(ventana,width=10,textvariable=result,justify="right")
            result.set(registro[5])
            txt_result.pack(pady=5)

            btn_guardar=Button(ventana, text="Guardar", command=lambda: funciones.Controladores.cambiar(num1.get(),num2.get(),signo.get(),result.get(),id.get()))
            btn_guardar.pack(pady=5)

            btn_volver=Button(ventana, text="Volver", command=lambda: Vistas.interfaz(ventana))
            btn_volver.pack(pady=5)
