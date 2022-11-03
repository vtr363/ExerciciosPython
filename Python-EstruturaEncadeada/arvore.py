#tentativa de implementação de arvore binaria

class NodoArvore:
    def __init__(self, dado):
        self.dado = dado
        self.direita = None
        self.esquerda = None

    def add(self, dado):
        if dado >= self.dado:
            if self.direita == None:
                self.direita = NodoArvore(dado)
            else:
                self.direita.add(dado)
        else:
            if self.esquerda == None:
                self.esquerda = NodoArvore(dado)
            else:
                self.esquerda.add(dado)

class Arvore:
    def __init__(self):
        self.root = None

    def add(self, dado):
        if not self.root:
            self.root = NodoArvore(dado)
        else:
            self.root.add(dado)

    def __search_engine(self, nodo, dado):
        
        if nodo.dado == dado:
            return nodo
        
        if dado >= nodo.dado:
            return self.__search_engine(nodo.direita, dado)
        else:
            return self.__search_engine(nodo.esquerda, dado)
    
    def search(self, dado):
        return self.__search_engine(self.root, dado)
    
    def __em_ordem(self, raiz):
        if not raiz:
            return
        
        self.__em_ordem(raiz.esquerda)
        print(raiz.dado)
        self.__em_ordem(raiz.direita)

    def mostra_em_ordem(self):
        self.__em_ordem(self.root)
    
    def max(self):
        current = self.root
        while current:
            current = current.direita
        return current
    
    def min(self):
        current = self.root
        while current:
            current = current.esquerda
        return current


    
arv = Arvore()
arv.add(1)
arv.add(2)
arv.add(6)
arv.add(4)
arv.mostra_em_ordem()
x = arv.search(4)
print(x.dado)
