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
       
def juntarLista(lista1, lista2):
    #terceiraLista = ListaEncadeada(lista1.cabeca, lista2.calda)
    terceiraLista = ListaEncadeada()
    atual = lista1.cabeca
    while atual is not None:
        terceiraLista.inserirFinal(atual)
        atual = atual.proximo

    atual = lista2.cabeca
    while atual is not None:
        terceiraLista.inserirFinal(atual)
        atual = atual.proximo

    return terceiraLista

lista1: 'ListaEncadeada' = ListaEncadeada()
lista1.inserirFinal(500)
lista1.inserirFinal(200)
lista1.inserirFinal(100)
lista1.inserirFinal(800)
lista1.inserirFinal(900)

lista2: 'ListaEncadeada' = ListaEncadeada()
lista2.inserirFinal(411)
lista2.inserirFinal(223)
lista2.inserirFinal(333)
lista2.inserirFinal(887)
lista2.inserirFinal(999)

lista3 = juntarLista(lista1, lista2)
lista3.imprimir()

