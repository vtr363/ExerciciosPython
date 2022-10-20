# Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. 
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

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

    def equals(self, pilha2):
        if self.__repr__() == pilha2.__repr__():
            return True
        return False


n = Pilha()
n.Add(1)
n.Add(2)
n.Add(3)
print(n)

p = Pilha()
p.Add(1)
p.Add(2)
p.Add(3)
print(p)

if n.equals(p): print("igual") 
else: print("diferente")