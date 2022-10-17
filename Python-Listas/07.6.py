from math import prod


vetor = list(map(int, input("Digite 5 numeros inteiros com apenas um(1) espaço entre eles: ").split()))
print('Soma: %d\nMultiplicação: %d\nNumeros: '+vetor %(sum(vetor), prod(vetor)))