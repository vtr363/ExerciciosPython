class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        if litros > self.quantidadeCombustivel:
            print("foram abastecidos %.2fL" % self.quantidadeCombustivel)
            self.quantidadeCombustivel = 0
        else:
            print("foram abastecidos %.2fL" % litros)
            self.quantidadeCombustivel -= litros

    def abastecePorLitro(self, litros):
        if litros > self.quantidadeCombustivel:
            valor = self.quantidadeCombustivel * self.valorLitro
            print("foram abastecidos R$: %.2f" % valor)
            self.quantidadeCombustivel = 0
        else:
            valor = litros * self.valorLitro
            print("foram abastecidos R$: %.2f" % valor)
            self.quantidadeCombustivel -= litros

    def alteraValor(self, novoValor):
        self.valorLitro = novoValor

    def alteraCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alteraQuantidadeCombustivel(self, quant):
        self.quantidadeCombustivel = quant


