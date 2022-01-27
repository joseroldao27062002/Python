class No:
    def __init__(self, carga = None, proximo = None, anterior = None):
        self.carga = carga
        self.anterior = anterior
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
       
class ListaDuplamenteEncadeada(ListaEncadeada):   
    def __init__(self):
        super().__init__()
        """
        self.cabeca = None
        self.cauda = None
        """
def remover_ocorrencias(valor, lista): 
    atual = lista.cabeca

    while atual is not None:
        if lista.cabeca.carga == valor:
            lista.cabeca = atual.proximo
            atual = atual.proximo
        else:
            if lista.cabeca.proximo.carga == valor:
                lista.cabeca.proximo = lista.cabeca.proximo.proximo
            atual = atual.proximo
        lista.imprimir()

lista = ListaDuplamenteEncadeada()
lista.inserirFinal(10)
lista.inserirFinal(10)
lista.inserirFinal(10)
lista.inserirFinal(50)
lista.inserirFinal(10)
lista.inserirFinal(10)
lista.imprimir()
remover_ocorrencias(10, lista)
lista.imprimir()
