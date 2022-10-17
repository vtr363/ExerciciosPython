from statistics import median


medias = []
for i in range(1, 3):
    medias.append(median(list(map(float, input("Digite as 4 notas do %d° aluno com apenas um(1) espaço entre elas: " %i).split()))))
aprovados = [i for i in medias if i >= 7]
print(len(aprovados))
