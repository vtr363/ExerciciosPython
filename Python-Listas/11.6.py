vetor1 = input("Digite os 10 elementos do 1° vetor com apenas um(1) espaço entre eles: ").split()
vetor2 = input("Digite os 10 elementos do 2° vetor com apenas um(1) espaço entre eles: ").split()
vetor3 = input("Digite os 10 elementos do 3° vetor com apenas um(1) espaço entre eles: ").split()
vetor4 = [val for pair in zip(vetor1, vetor2, vetor3) for val in pair]
print(vetor4)
