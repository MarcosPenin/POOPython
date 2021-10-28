
class DNI():
    def __init__(self,numero):
        self.__numero=numero
    
    def calcularLetra(self):
        letras="TRWAGMYFPDXBNJZSQVHLCKE"       
        self.__letra= letras[int(self.__numero)%23]
        return self.__letra
    
    @property
    def numero(self):
        return self.__numero
    @property
    def letra(self):
        return self.__letra

    @numero.setter
    def numero(self,numero):
        if len(numero)==8 and numero.isdigit():
            self.__numero=numero
            self.__letra=self.calcularLetra()
        else:
            self.__numero=0
            self.__letra=""
            print("DNI INCORRECTO")   
    
    def mostrar(self):
        return self.numero,self.letra

