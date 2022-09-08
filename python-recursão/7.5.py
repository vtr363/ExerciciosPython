# Crie um programa que receba um vetor de números reais com 100 elementos.
# Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor.

def inverte(vet):
    if len(vet) == 1:
        return vet
    print(vet[0])
    return inverte(vet[1:]) + [vet[0],]

lista = []
for i in range(100):
    lista.append(i)

print(inverte(lista))