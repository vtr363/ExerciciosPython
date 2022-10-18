from statistics import mean


altura = []
idade = []
for i in range(30):
    x, y = input('Digite a ideda e altura do aluno com apenas 1(um) espaço entre elas: ').split()
    altura.append(x)
    idade.append(y)
alunos = [i for index, i in enumerate(altura) if i < mean(altura) and idade[index] > 13]
print(len(alunos))
