class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostraPonto(self):
        print("x: %.1f\ny: %.1f" % (self.x, self.y))


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontraCentro(self):
        Ponto(self.altura / 2, self.largura / 2).mostraPonto()


r1 = Retangulo(5, 5)
r1.encontraCentro()