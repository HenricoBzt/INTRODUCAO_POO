class Conta:
    def __init__(self,nmr_agencia,saldo=0):
        self._saldo = saldo
        self.agencia = nmr_agencia
    
    def depositar(self,valord):
        self._saldo += valord
    
    def sacar(self,valorsq):
        self._saldo -= valorsq

    def mostrar_saldo(self):
        return self._saldo
conta = Conta("001",100)
# conta._saldo += 100 ==> !NÃO DEVO FAZER ISSO!!
conta.depositar(100)
print(conta.mostrar_saldo())

