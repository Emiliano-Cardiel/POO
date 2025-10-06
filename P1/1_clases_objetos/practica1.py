'''
  Practica #1 Implementar paradigma estructurado VS OO
  Crear un programa que obtenga el área de un rectángulo
'''
import os

#1.-Estructurado
#Procedimiento
def proceso():
    os.system("cls")
    print("\n\t Calculo para sacar area de un rectángulo \t")
    base=float(input("\n\tIngresa el valor de la base: "))
    altura=float(input("\tIngresa el valor de la altura: "))
    area=base*altura
    print(f"\n\t\t El área de tu rectángulo es: {area} \t")

proceso()

#Función
def areaRectangulo(base,altura):
    area=base*altura
    return area

base=6
altura=7
print(f"\n\t\t El área de tu rectángulo es: {areaRectangulo(base,altura)} \t")
input("\n\tPresione una tecla para continuar")

#2.-OO
#Sin atributos
os.system("cls")
class AreaRectangulo:
    def areaRectangulo(self,base,altura):
        area=base*altura
        return area
    
rectangulo1=AreaRectangulo()    #Instanciar un objeto de la clase "AreaRectangulo"
print(f"\n\t\t El área de tu rectángulo es: {rectangulo1.areaRectangulo(base,altura)} \t")

#Con atributos
os.system("cls")
class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def areaRectangulo(self):
        area=self.base*self.altura
        return area
    
rectangulo1=AreaRectangulo(5,6)    #Instanciar un objeto de la clase "AreaRectangulo"
print(f"\n\t\t El área de tu rectángulo es: {rectangulo1.areaRectangulo()} \t")