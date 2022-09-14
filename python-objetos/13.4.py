class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = str(nome)
        self.__salario = float(salario)

    def mostraFuncionario(self):
        return self.__nome, self.__salario


jao = Funcionario("jão", 1200)
jao.mostraFuncionario()