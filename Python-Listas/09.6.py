x = lambda x : pow(x, 2)
A = sum(list(map(x, list(map(int, input("Digite 10 numero com apenas um(1) espaço entre eles: ").split())))))
print(A)