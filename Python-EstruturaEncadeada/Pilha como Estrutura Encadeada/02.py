# Utilizando uma pilha resolver o exercício a seguir: 
# Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.
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
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next

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

n = Pilha()
n.Add(1)
n.Add(2)
n.Add(3)
print(n)
print(n.Reversed().split())