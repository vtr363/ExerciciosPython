# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, 
# um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários 
# nos seguintes intervalos de valores:

#     $200 - $299
#     $300 - $399
#     $400 - $499
#     $500 - $599
#     $600 - $699
#     $700 - $799
#     $800 - $899
#     $900 - $999
#     $1000 em diante

# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
from math import floor


print('Digite (-1) para finalizar\n')
bruto = []
vendas = {'200': 0, 
        '300': 0,
        '400': 0,
        '500': 0,
        '600': 0,
        '700': 0,
        '800': 0,
        '900': 0,
        '1000': 0}
while (True):
    val = float(input('Digite o valor bruto das vendas da semana: '))
    if val == -1:
        break
    bruto.append(val)

for i in bruto:
    val = str(floor(i/100)*100)
    if val in vendas:
        vendas[val] += 1

print(vendas)

