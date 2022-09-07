# Faça uma função recursiva que permita somar os elementos de um vetor de inteiros. 
def soma(number):
    if number == []:
        return 0
    else:
        return  soma(number[1:]) + number[0]
print(soma([1, 2, 3]))