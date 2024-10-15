class Estudante:
    faculdade = "Uninassau"

    def __init__(self,nome,nmr_matricula):
        self.nome = nome 
        self.nmr_matricula = nmr_matricula
    
    def __str__(self):
        return f"{(self.nome)} --- {(self.nmr_matricula)} --- {(self.faculdade)}"

def mostrar_valor(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Junio",1711409)
aluno_2 =Estudante("Baza",1711567)


mostrar_valor(aluno_1,aluno_2)

aluno_1.nmr_matricula = 1711789
aluno_3 = Estudante("Alfredo",1712157)
aluno_3.faculdade = "Unibra"
print("==========Atualizado=========")
mostrar_valor(aluno_1,aluno_2,aluno_3)