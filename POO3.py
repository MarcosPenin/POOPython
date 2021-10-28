"""Ejercicio 3
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la
cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
Construye los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por
lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular
es mayor de edad pero menor de 25 años y falso en caso contrario.
• Además la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de
la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir"""

from DNI import DNI
from POO1 import Persona
from POO2 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular=Persona, cantidad=0, bonificacion=0):
        super().__init__(titular,cantidad)
        self.__bonificacion=bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,bonificacion):    
        self.__bonificacion=bonificacion
            
    def esTitularValido(self):
        if self.titular.edad>24 or self.titular.edad<18:
            valido=False
        else:
            valido=True
        return valido

    def retirar(self, retirada):
        if self.esTitularValido():
            super().retirar(retirada)
        else:
            print("Lo siento, el usuario no es válido. Pase por su banco para más información")

    def mostrar(self):
        print("DATOS DE LA CUENTA")
        super().titular.mostrar()
        print("Cuenta joven. Cantidad:",self.cantidad,"Bonificación:",self.__bonificacion,"%")



dni1=DNI(39453679)
dni1.calcularLetra()
persona1=Persona("Marcos",33,dni1)
persona2=Persona("Juana",23,dni1)
cuentaJoven1=CuentaJoven(persona1,1000,10)
cuentaJoven2=CuentaJoven(persona2,500)

print("La bonificación es del",cuentaJoven2.bonificacion,"%")
cuentaJoven2.bonificacion=15
print("La bonificación es del",cuentaJoven2.bonificacion,"%")
cuentaJoven2.mostrar()
cuentaJoven1.retirar(100)
cuentaJoven2.retirar(100)
