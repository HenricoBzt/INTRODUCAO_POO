class Bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plim.. Plimm..')
    
    def pedalar(self):
        print('Pedalando...')

    def freiar(self):
        print('Freiando...')

    def parar(self):
        print('Bicicleta parada.')
    
    # def __str__(self):
    #     return f'Informações da bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}'

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"

b1 = Bicicleta("Azul", "Caloi", 2024, 1200)
b1.buzinar()
b1.pedalar()
b1.freiar()
b1.parar()
print(b1)
