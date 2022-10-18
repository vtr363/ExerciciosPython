from operator import index
from statistics import mean


tempMes = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for item in meses:
    tempMes.append(input("digite a temperatura media do mes de {meses[item][0]}"))
media = mean(tempMes)
hot = [i for index, i in enumerate(meses) if tempMes[index] > media]
print(hot)