# Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. 
def somatorio(numero):
    if numero == 0:
        return 0
    else:
        return somatorio(numero-1) + numero

print(somatorio(4))