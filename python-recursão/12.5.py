# Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente.
def contador(n):
    if n == 0:
        return [0,]
    
    return contador(n-1) + [n, ]

print(contador(6))