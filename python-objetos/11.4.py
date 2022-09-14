class Carro:
    def __init__(self, consumo):
        self.__consumo = consumo
        self.__tanque = 0

    def andar(self, distancia):
        self.__tanque -= (distancia / self.__consumo)

    def obterGasolina(self):
        return self.__tanque

    def adicionaGasolina(self, litros):
        self.__tanque += litros
