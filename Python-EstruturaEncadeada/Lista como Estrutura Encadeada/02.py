# Remova duplicatas de uma lista ordenada. Suponha que lhe seja fornecida uma lista encadeada armazenando 
# números inteiros em ordem crescente. Sua tarefa é remover todos os elementos duplicados da lista. 
# Por exemplo, dada a lista [0 → 1 → 1 → 5 → 7 → 10 → 10 → None], 
# seu programa deve retornar a lista [0 → 1 → 5 → 7 → 10 → None].
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
            current.previous.next = current.next
        else:
            self.head = self.head.next
            
    def RemoveDuplicates(self):
        current = self.head
        while current != None:
            if current.next and current.dado == current.next.dado:
                current.next = current.next.next
            else:
                current = current.next
            


n = Lista()
n.Add(2)
n.Add(2)
n.Add(3)
n.RemoveDuplicates()
print(n)