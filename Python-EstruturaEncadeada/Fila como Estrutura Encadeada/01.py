class Nodo:
    def __init__(self, dado = None, proximo = None, previous = None):
        self.dado = dado
        self.proximo = proximo

    def __repr__(self):
        return str(f"{self.dado} -> {self.proximo}")

class Fila:
    def __init__(self):
        self.cabeca = None
    
    def __repr__(self):
        return str(self.cabeca)
    
    def AdicionaNoFim(self, dado):
        self.cabeca = Nodo(dado, self.cabeca)
        if self.cabeca.proximo:
            proximo = self.cabeca.proximo
    
    def pop(self):
        if self.cabeca:
            self.cabeca = self.cabeca.proximo
        
    def busca(self, dado):
        current = self.cabeca
        index = 0
        while current.dado != dado and current != None:
            current = current.proximo
            index +=1
        if not current:
            return None
        return index