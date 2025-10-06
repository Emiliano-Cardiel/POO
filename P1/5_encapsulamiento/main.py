#Instanciar los objetos para posteriormente implementarlos
from coches import Coches
import os

os.system("cls")
num_coches=int(input("¿Cúantos coches deseas? "))

for i in range(0,num_coches):
    print(f"\n\t... Datos del Coche {i+1}...")
    marca=input("Ingresa la Marca: ").upper()
    color=input("Ingresa el Color: ").upper()
    modelo=input("Ingresa el Modelo: ").upper()
    velocidad=int(input("Ingresa la Velocidad: "))
    caballaje=int(input("Ingresa el Caballaje: "))
    plazas=int(input("Ingresa las Plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,caballaje,plazas)
    
    print(f"Los datos del Coche 1 son: \nMarca: {coche1.marca} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

    print(f"\n\t {coche1.frenar()}")



#Múltiples objetos
# coche1=Coches("VW","Blanco","2022",220,150,5)
# coche2=Coches("Nissan","Azul","2020",180,150,6)
# coche3=Coches("Honda","","",0,0,0)

# print(f"Las marca del Coche 1 son: \nMarca: {coche1.marca} \nColor: {coche1.getColor()} \nModelo: {coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballaje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

# print(f"\nLas marca del Coche 2 son: \nMarca: {coche2.getMarca()} \nColor: {coche2.getColor()} \nModelo: {coche2.getModelo()} \nVelocidad: {coche2.getVelocidad()} \nCaballaje: {coche2.getCaballaje()} \nPlazas: {coche2.getPlazas()}")

# print(coche3.marca)