# 1. Implemente a função remove utilizando a função busca. 
class Nodo:
    def __init__(self, dado = None, next = None, previous = None):
        self.dado = dado
        self.next = next
        self.previous = previous

    def __repr__(self):
        return str(f"{self.dado} -> {self.next}")


class Lista:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return str(self.head)
    
    def Add(self, dado):
        self.head = Nodo(dado, self.head)
        if self.head.next:
            next = self.head.next
            next.previous = self.head

    def FindFirst(self, dado):
        current = self.head
        while current.dado != dado and current != None:
            current = current.next
        return current
    
    def Remove(self, dado):
        current = self.FindFirst(dado)
        if current and current.previous:
            previous = current.previous
            previous.next = current.next
        else:
            self.head = self.head.next
            
    


n = Lista()
n.Add(2)
n.Add(2)
n.Add(3)
n.Remove(3)
print(n)