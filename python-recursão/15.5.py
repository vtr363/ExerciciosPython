# Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente. 
def contador(n):
    if n == 0:
        return [0,]
    
    return [n, ] + contador(n-2)

print(contador(6))