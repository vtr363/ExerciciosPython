# Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um: 

#     se positivo, inserir na pilha P; 
#     se negativo, inserir na pilha N; 
#     se zero, retirar um elemento de cada pilha.

class Nodo:
    def __init__(self, dado = None, next = None, previous = None):
        self.dado = dado
        self.next = next
        self.previous = previous

    def __repr__(self):
        return str(f"{self.dado} -> {self.next}")


class Pilha:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        return str(self.head)
    
    def Add(self, dado):
        self.head = Nodo(dado, self.head)
        if self.head.next:
            next = self.head.next
            next.previous = self.head
        else:
            self.tail = self.head

    def Remove(self):
        if self.head:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
        return self.head

    def FindFirst(self, dado):
        current = self.head
        while current.dado != dado and current != None:
            current = current.next
        return current

    def GreatestElemente(self):
        current = self.head
        greatest = self.head.dado
        while current != None:
            if current.dado > greatest: greatest = current.dado
            current = current.next
        return greatest

    def Reversed(self):
        current = self.tail
        response = ['None']
        while current:
            response.append(current.dado)
            current = current.previous
        return " -> ".join(map(str, response))

    def allOut(self):
        while(self.head):
            print(self.Remove())


def Tpilha2(n, p, vet):
    for i in vet:
        if i > 0: n.Add(i)
        elif i < 0: p.Add(i)
        elif i == 0: 
            n.Remove()
            p.Remove()

vetor = []
pilha1 = Pilha()
pilha2 = Pilha()
Tpilha2(pilha1, pilha2, vetor)

