from math import floor


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudaLados(self,  comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mostraLados(self):
        return self.comprimento, self.largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return self.comprimento * 2 + self.largura * 2


x, y = input("informe as medidas do local:\n"
             "ex: 23 15\n").split()
local = Retangulo(float(x), float(y))

x, y = input("informe as medidas do piso:\n"
             "ex: 5 3\n").split()
piso = Retangulo(float(x), float(y))

quantidade = local.area() / piso.area()

print("serão necessarios %d pisos" % (floor(quantidade)))