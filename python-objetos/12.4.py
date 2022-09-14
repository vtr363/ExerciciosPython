class ContaDeInvestimento:
    def __init__(self, numeroConta, nomeCorrentista, taxaJuros, saldo=0):
        self.__numeroConta = numeroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

        self.__taxaJuros = taxaJuros

    def alteraNome(self, nome):
        self.__nomeCorrentista = nome

    def deposito(self, quantidade):
        self.__saldo = self.__saldo + quantidade

    def saque(self, quantidade):
        self.__saldo = self.__saldo - quantidade

    def adicionaJuros(self):
        self.__saldo *= (self.__taxaJuros/100) + 1

    def mostraSaldo(self):
        return self.__saldo


poupanca = ContaDeInvestimento(1, "Jão", 10, 1000)
poupanca.adicionaJuros()
poupanca.adicionaJuros()
poupanca.adicionaJuros()
poupanca.adicionaJuros()
poupanca.adicionaJuros()
print(poupanca.mostraSaldo())
