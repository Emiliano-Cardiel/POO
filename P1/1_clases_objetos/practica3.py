import os 
os.system("cls")

class Profesores():
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def impartir(self):
        pass

    def evaluar(self):
        pass

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self,experiencia):
        self.__experiencia=experiencia

    @property
    def num_profesor(self):
        return self.__num_profesor
    
    @num_profesor.setter
    def num_profesor(self,num_profesor):
        self.__num_profesor=num_profesor

class Alumnos():
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    def inscribirse(self):
        # print("El alumno se inscribe a clases") Mala práctica
        return "El alumno se inscribe a clases"

    def estudiar(self):
        pass

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula

class Cursos():
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def asignar(self):
        pass

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo

    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self,creditos):
        self.__creditos=creditos

profesor1=Profesores("Ana Torres Guzman",40,123)
profesor2=Profesores("Daniel Contreras",35,124)
print(profesor1.nombre,profesor1.experiencia,profesor1.num_profesor)
print(profesor2.nombre,profesor2.experiencia,profesor2.num_profesor)

alumno1=Alumnos("Juan Correa Simental",25,100123)
alumno2=Alumnos("María Serrano Mata",22,100124)
print(alumno1.nombre,alumno1.edad,alumno1.matricula)
print(alumno2.nombre,alumno2.edad,alumno2.matricula)

curso1=Cursos("POO",100,6)
curso2=Cursos("FOSO",101,4)
print(curso1.nombre,curso1.codigo,curso1.creditos)
print(curso2.nombre,curso2.codigo,curso2.creditos)