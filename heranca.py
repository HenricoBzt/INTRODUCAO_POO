class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_roda = numero_rodas
        
    def Ligarmotor(self):
        print("Ligando motor..")
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("preta","FGVC987",2)

moto.Ligarmotor()

