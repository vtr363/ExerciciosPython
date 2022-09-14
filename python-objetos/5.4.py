class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo = 0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alteraNome(self, nome):
        self.nomeCorrentista = nome

    def deposito(self, quantidade):
        self.saldo = self.saldo + quantidade

    def saque(self, quantidade):
        self.saldo = self.saldo - quantidade