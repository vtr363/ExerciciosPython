 # Crie um programa que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule kn . Utilize apenas multiplicações. 
 # O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função. 
def exponencial(k, n):
    if n == 0: 
        return 1
    else: 
        return exponencial(k, n-1) * k
print(exponencial(2, 10))