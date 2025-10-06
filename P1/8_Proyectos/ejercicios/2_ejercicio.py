'''
Realizat un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizat un método para cada una e imprimir los resultados obtenidos. LLamar a la clase Calculadora.
'''

# class Calculadora():
#     def __init__(self,num1,num2):
#         self._num1=num1
#         self._num2=num2

#     @property
#     def num1(self):
#         self._num1
    
#     @num1.setter
#     def num1(self,num1):
#         self._num1=num1

#     @property
#     def num2(self):
#         self._num2
    
#     @num2.setter
#     def num2(self,num2):
#         self._num2=num2

#     def suma (self,num1,num2):
#         self._num1=num1
#         self._num2=num2
#         sum=num+num2
#         return sum
    
#     def resta (self,num1,num2):
#         self._num1=num1
#         self._num2=num2
#         rest=num1+num2
#         return rest
    
#     def multi (self,num1,num2):
#         self._num1=num1
#         self._num2=num2
#         mult=num1*num2
#         return mult
    
#     def divi (self,num1,num2):
#         self._num1=num1
#         self._num2=num2
#         div=num1/num2
#         return div
    
# num1=int(input("Ingresa un número"))
# num2=int(input("Ingresa otro número"))

# numeros=Calculadora(num1,num2)
# print(numeros.suma)
# print(numeros.resta)
# print(numeros.multi)
# print(numeros.divi)

class Calculadora:
    def __init__(self):
        self._numero1=int(input("Numero #1: "))
        self._numero2=int(input("Numero #2: "))

    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self,numero1):
        self._numero1=numero1

    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self,numero2):
        self._numero2=numero2

    def sumar(self):
        return self._numero1+self._numero2

    def restar(self):
        return self._numero1-self._numero2   

    def multiplicar(self):
        return self._numero1*self._numero2
    
    def dividir(self):
        return self._numero1/self._numero2
    
operacion=Calculadora()
print(f"{operacion.numero1}+{operacion.numero2}{operacion.sumar()}")
print(f"{operacion.numero1}-{operacion.numero2}{operacion.restar()}")
print(f"{operacion.numero1}*{operacion.numero2}{operacion.multiplicar()}")
print(f"{operacion.numero1}/{operacion.numero2}{operacion.dividir()}")