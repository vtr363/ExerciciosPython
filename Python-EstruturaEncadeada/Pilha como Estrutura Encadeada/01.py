# Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.
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
    
    def __repr__(self):
        return str(self.head)
    
    def Add(self, dado):
        self.head = Nodo(dado, self.head)
        if self.head.next:
            next = self.head.next
            next.previous = self.head

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