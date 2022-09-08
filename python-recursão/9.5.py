# Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. 

def somatorio(n):
    if n == 1:
        return 1
    return somatorio(n-1) + n

print(somatorio(3))