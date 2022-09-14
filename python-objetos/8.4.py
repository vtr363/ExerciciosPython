class Macaco:
    def __init__(self, comida=None):
        self.bucho[0] = comida

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = None


m1 = Macaco("banana")
m1.comer("pera")
m2 = Macaco(m1)
