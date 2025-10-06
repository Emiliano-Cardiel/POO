import os
#Instanciar los objetos para posterior implementarlos
from coches import *


# os.system("cls")
# coche=Coches("VW","Blanco","2020",220,200,5)
# print(coche.marca, coche.acelerar())
    
# camioneta=Camionetas("Chevrolet","Rojo","2021",180,150,5,"4x4",False)
# print(camioneta.marca, camioneta.acelerar())

# camion=Camiones("Volvo","Azul","2019",140,400,3,4,10000)
# print(camion.marca, camion.acelerar())

# num_coche=int(input("Cuantos coches desea ingresar: "))
# for i in range(0,num_coche):
#     print(f"\n\t ..::Datos del Coche {i+1}::..")
#     marca=input("Ingrese la marca del coche: ").upper()
#     color=input("Ingrese el color del coche: ").upper()
#     modelo=input("Ingrese el modelo del coche: ").upper()
#     velocidad=int(input("Ingrese la velocidad del coche: "))
#     caballaje=int(input("Ingrese el caballaje del coche: "))
#     plazas=int(input("Ingrese las plazas del coche: "))

# coche1=Coches(marca,color,modelo,velocidad,caballaje,plazas)

# print(f"Las marca del Coche 1 son: \nMarca: {coche1.getMarca()} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

# print(f"\n{coche1.acelerar()}")

def borrar_pantalla():
    os.system("cls")

def espereTecla():
    input("\n\t::Oprime una tecla para continuar::")

def datos_autos(tipo):
    borrar_pantalla()
    print(f"\n\t ..::Ingresar los datos del vehiculo de tipo {tipo}::..")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    caballaje=int(input("Caballaje: "))
    plazas=int(input("No. # de plazas: "))
    return marca,color,modelo,velocidad,caballaje,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,caballaje,plazas):
    print(f"Los datos del Vehiculo son: \nMarca: {marca} \nColor: {color} \nModelo: {modelo} \nVelocidad: {velocidad} \nCaballaje: {caballaje} \nPlazas: {plazas}")

def autos():
    os.system("cls")
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Auto")
    coche=Coches(marca,color,modelo,velocidad,caballaje,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

def camionetas():
    os.system("cls")
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Camioneta")
    traccion=(input("Tracción: ")).upper()
    cerrada=(input("¿Cerrada (SI/NO)?: ")).upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False

    coche=Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
    
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"\nTracción: {coche.traccion} \nCerrada: {coche.cerrada}")

def camiones():
    os.system("cls")
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("Camion")
    eje=int(input("No. # de Ejes: "))
    capacidadCarga=int(input("Capacidad de Carga: "))

    coche=Camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)

    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"\nEjes: {coche.eje} \nCapacidad de Carga: {coche.capacidadCarga}")

def main():
    borrar_pantalla()
    opcion=True
    while opcion:
        print("\n\t\t..::Menu Principal::.. \n1.- Autos \n2.- Camionetas \n3.- Camiones\n4.- Salir")
        opcion=input("Ingrese una opcion: ").lower().strip()
        match opcion:
            case"1":
                autos()
                espereTecla()
            case"2":
                camionetas()
                espereTecla()
            case"3":
                camiones()
                espereTecla()
            case"4":
                borrar_pantalla()
                print("\n\t\tGracias por su visita")
                espereTecla()
                opcion=False
            case _:
                print("\n\tOpcion incorrecta, intente de nuevo")
                espereTecla()

if __name__=="__main__":
    main()

