class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def alteraLado(self, novoLado):
        self.lado = novoLado

    def mostraLado(self):
        print(self.lado)

    def areaQuadrado(self):
        print(self.lado ** 2)