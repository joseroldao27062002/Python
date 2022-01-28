class TabelaHash:
    def __init__(self):
        self.__tamanho = 50
        self.__vetor = [None] * self.__tamanho

    @property
    def vetor(self):
        return self.__vetor
 
    def funcaoHash(self, chave):
        return hash(chave) % self.__tamanho

    def adicionarItem(self, chave, valor):
        indice = self.funcaoHash(chave)        
        self.__vetor[indice] = valor

    def obterItem(self, chave): 
        indice = self.funcaoHash(chave)        
        return self.__vetor[indice]

    def deletarItem(self, chave): 
        indice = self.funcaoHash(chave)
        self.__vetor[indice] = None

    def reHash(self, chave, computador):
        if self.__vetor[chave] != None:
            reHash(self, chave + 1)
        else:
            self.adicionarItem(self, chave, computador.macAddress)
