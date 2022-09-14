class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for i in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1

    def engordar(self, peso):
        self.peso = self.peso + peso

    def emagrecer(self, peso):
        self.peso = self.peso - peso

    def crescer(self, altura):
        self.altura = self.altura + altura


p = Pessoa("j", 15, 45, 167)

p.en