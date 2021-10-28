from DNI import DNI
from POO1 import Persona


class Cuenta():
    def __init__(self,titular=Persona):
        self.__titular=titular

    def __init__(self,titular=Persona,cantidad=0):
        self.__titular=titular
        self.__cantidad=cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):    
        self.__titular=titular

    def ingresar(self,ingreso):
        if ingreso>0:
            self.__cantidad+=ingreso
            print("Ha ingresado",ingreso,"euros")
        else:
            print("No puede ingresar una cantidad negativa")
    
    def retirar(self,retirada):
        if retirada>0:
            self.__cantidad-=retirada
            print("Ha retirado",retirada,"euros")
        else:
            print("No puede retirar una cantidad negativa")

    def mostrar(self):
        print("DATOS DE LA CUENTA")
        self.titular.mostrar()
        print("Cantidad: ",self.cantidad)







