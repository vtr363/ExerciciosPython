vetor = input("Digite 10 caracteres: ")
cons = [i for i in vetor if ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')) and i not in 'aeiouAEIOU']
print((cons))