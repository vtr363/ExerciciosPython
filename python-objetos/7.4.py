class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alteraNome(self, nome):
        self.nome = nome

    def alteraFome(self, fome):
        self.fome = fome

    def alteraSaude(self, saude):
        self.saude = saude

    def alteraIdade(self, idade):
        self.idade = idade

    def mostraNome(self):
        return self.nome

    def mostraFome(self):
        return self.fome

    def mostraSaude(self):
        return self.saude

    def mostraHumor(self):
        return (self.saude + self.fome) / 2
