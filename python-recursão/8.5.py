# O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y.
# Escreva uma função recursiva mdc, que retorna o máximo divisor comum de x e y.
# O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto. 
def mdc(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    if max(x, y) % min(x, y) == 0:
        return min(x, y)

    for i in range(min(x, y)-1, 1, -1):
        if min(x, y) % i == 0:
            return mdc(i, max(x, y))
    return 0

print(mdc(12, 8))