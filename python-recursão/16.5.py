# A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 Faça uma função recursiva que receba um número inteiro positivo impar N
# e retorne o fatorial duplo desse número.

def fatorialDuplo(num):
    if num%2==0:
        num-=1
    if num <= 0:
        return 1
    else:
        return fatorialDuplo(num-2) * num

print(fatorialDuplo(5))