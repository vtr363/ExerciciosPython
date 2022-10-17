vetor = list(map(int, input("Digite 20 numeros inteiros com apenas um(1) espaço entre eles: ").split()))
par = [i for i in vetor if i % 2 == 0]
impar = [i for i in vetor if i not in par]
print("Par: "+ par + "\nimpar: "+impar+"\nTodos: "+ vetor)