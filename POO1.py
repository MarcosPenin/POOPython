"""Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
Construye los siguientes métodos para la clase: 
• Un constructor, donde los datos pueden estar vacíos. 
• Los setters y getters para cada uno de los atributos. 
Hay que validar las entradas de datos. 
• mostrar(): Muestra los datos de la persona. 
• esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad. """

from DNI import DNI

class Persona():
    
    def __init__(self,nombre="", edad="",DNI=DNI):
        self.__nombre=nombre
        self.__edad=edad
        self.__DNI=DNI
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    @nombre.setter
    def nombre(self,nombre):    
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):
        if edad.isdigit():
            self.__edad=edad
        else:
            print("La edad debe tener un valor númerico")
            
    @DNI.setter
    def DNI(self,x):
        if isinstance(x,DNI):
            self.__DNI=DNI
        else:
            print("No ha introducido un DNI")

    def mostrar(self):
        print("Nombre:",self.nombre, "Edad:",self.edad, "DNI:",self.DNI.mostrar())
    
    def esMayorDeEdad(self):
        if self.__edad>17:
            flag=True
        else:
            flag=False
        return flag

