# Construa um programa utilizando uma pilha que resolva o seguinte problema: 

#     Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. 
#     Dado uma placa verifique se o carro está estacionado na rua. 
#     Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.



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
    
    def FindIndex(self, dado):
        current = self.head
        index = 0
        while current.dado != dado and current != None:
            current = current.next
            index += 1
        return index

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

    def sequenceToRemove(self, dado):
        index = (self.FindIndex(dado)*2)+1
        rev = self.Reversed().split()
        return "".join(rev[index:])

    def equals(self, pilha2):
        if self.__repr__() == pilha2.__repr__():
            return True
        return False


road = Pilha
resp = "1"
while resp != "4":
    resp = input("1 - Estacionar carro\n"
        "2 - Mostrar sequencia para retirar o carro\n"
        "3 - Remove o carro mais a frente\n"
        "4 - Finalizar\n")
    match resp:
        case "1":
            plate = input("Digite a placa do carro: ")
            print(plate)
            road.Add(123)
        case "2":
            plate = input("Digite a placa do carro: ")
            if road.FindFirst(plate):
                road.sequenceToRemove(plate)
            else:
                print("Carro não encontrado")
        case '3':
            road.Remove()
        case '4':
            print("Finalizando")
            break
        case _:
            print("Opção Invalida")
                
            


