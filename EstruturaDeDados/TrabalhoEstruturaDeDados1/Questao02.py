class No:
    def __init__(self, carga = None, proximo = None):
        self.carga = carga
        self.proximo = proximo

    def __str__(self):
        return str(self.carga)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.calda = None

    def inserirInicio(self, valor):
        no = No(valor)
        if self.cabeca == None and self.calda == None:
            self.cabeca = self.calda = no
        else:
            no.proximo = cabeca.carga
            self.cabeca = no

    def inserirFinal(self, valor):
        no = No(valor)
        if self.cabeca == None and self.calda == None:
            self.cabeca = self.calda = no
        else:
            self.calda.proximo = no
            self.calda = no

    def imprimir(self):
        if self.cabeca == None:
            print('ListaVazia')
            return
        else:
            atual = self.cabeca
            while atual is not None:
                print(str(atual.carga), end = ' ')
                atual = atual.proximo
        print()
       
def extraiParesImpares(lista):
    listaEncadeadaImpar = ListaEncadeada()
    listaEncadeadaPar = ListaEncadeada()
    
    atual = lista.cabeca
    while atual is not None:
        if atual.carga % 2 == 0:
            listaEncadeadaPar.inserirFinal(atual.carga)
        else:
            listaEncadeadaImpar.inserirFinal(atual.carga)
        atual = atual.proximo

    return listaEncadeadaPar, listaEncadeadaImpar
        

lista = ListaEncadeada()
lista.inserirFinal(1)
lista.inserirFinal(2)
lista.inserirFinal(6)
lista.inserirFinal(7)
lista.inserirFinal(8)

lista.imprimir()
pares, impares = extraiParesImpares(lista)
print("Pares =")
pares.imprimir()
print("Ímpares =")
impares.imprimir()

