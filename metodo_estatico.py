class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nasscimento(cls,ano,nome):
        idade = 2024 - ano
        return Pessoa(nome,idade)
    
    @staticmethod
    def maior_de_idade(idade):
        if idade >= 18:
            print("Maior de idade")
        else:
            print("Menor de idade")

#metodo de classe
p = Pessoa.criar_data_nasscimento(2006,"Henrico")
print(p.nome, p.idade)

#metodo estatico
print(Pessoa.maior_de_idade(18))
print(Pessoa.maior_de_idade(8))