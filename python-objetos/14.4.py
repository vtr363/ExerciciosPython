class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = str(nome)
        self.__salario = float(salario)

    def mostraFuncionario(self):
        return self.__nome, self.__salario

    def aumentaSalario(self, percentualDeAumento):
        self.__salario *= (percentualDeAumento/100)+1

jao = Funcionario("jão", 1000)
jao.aumentaSalario(10)
print(jao.mostraFuncionario())
