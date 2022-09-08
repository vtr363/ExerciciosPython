# Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci.
# Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89... 
def fibonacci(n, atual=1, anterior=0):
    if n == 1:
        return atual
    return fibonacci(n-1, atual+anterior, atual)

print(fibonacci(7))