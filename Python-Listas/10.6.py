vetor1 = input("Digite os 10 elementos do 1° vetor com apenas um(1) espaço entre eles: ").split()
vetor2 = input("Digite os 10 elementos do 2° vetor com apenas um(1) espaço entre eles: ").split()
vetor3 = [val for pair in zip(vetor1, vetor2) for val in pair]
print(vetor3)

