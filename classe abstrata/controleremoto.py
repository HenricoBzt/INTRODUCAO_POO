from abc import ABC, abstractclassmethod, abstractproperty

#Controle remoto vai ser a minha interface
class ControleRemoto(ABC):
    @abstractclassmethod
    def Ligar(self):
        pass

    @abstractclassmethod
    def Desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
     def Ligar(self):
        print("Ligando Tv..")
        print("Tv Ligada!!")

     def Desligar(self):
        print("Desligando tv...")
        print("Tv desligada!")

     def marca(self):
         return "Philips"

class Controle_Arcondicionado(ControleRemoto):
    def Ligar(self):
        print("Ligando Ar condicionado..")
        print("Ar condicionado  Ligado!!")

    def desligar(self):
        print("Desligando Ar condicionado..")
        print("Ar condicionado desligado!!")

    def marca(self):
         return "LG"

controle = ControleTv()

controle.Ligar()
controle.Desligar()

