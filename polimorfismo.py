class Passaro:
    def voar(self):
        print("Voando..")

class Pardal(Passaro):
    def voar(self):
       print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar!")


# FIXO: EXEMPLO MEIA BOMBA 
# \/  \/  \/  \/  \/  \/  \/
class Aviao(Passaro):
    def voar(self):
        print("Decolando..")
    
def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())