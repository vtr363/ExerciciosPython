from audioop import reverse
from statistics import median


medidas = []
for i in range(1, 6):
    medidas.append(list(map(reverse, input("Digite sua idade e alturta com apenas um(1) espaço entre elas: " %i).split())))
print(medidas)

