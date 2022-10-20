#  Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue: 

#     Se o número for par, insira-o na pilha; 
#     Se o número lido for ímpar, retire um número da pilha; 
#     Ao final, esvazie a pilha imprimindo os elementos.

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

vetor = []
Tpilha = Pilha()
for i in vetor:
    if i%2 ==0: Tpilha.Add(i)
    else: Tpilha.Remove() 

