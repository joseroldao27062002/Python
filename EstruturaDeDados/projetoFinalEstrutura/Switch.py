from Dispositivo import Dispositivo
class Switch(Dispositivo):
    def __init__(self, ipAddress, macAddress, quantidadePortas):
        super().__init__(ipAddress, macAddress)
        self.__quantidadePortas = quantidadePortas
        self.__tabelaRoteamento = [] 
        self.criarTabelaRoteamento() 
    
    def criarTabelaRoteamento(self):
        for i in range(0, self.__quantidadePortas):
            self.tabelaRoteamento.append([None, None])

        #Métodos getter
    @property
    def quantidadePortas(self):
        return self.__quantidadePortas

    @property
    def tabelaRoteamento(self):
        return self.__tabelaRoteamento

    @property
    def computadores(self):
        return self.__computadores

    #Métodos setter
    @quantidadePortas.setter
    def quantidadePortas(self, quantidadePortas):
        self.__quantidadePortas = quantidadePortas
    
    @tabelaRoteamento.setter
    def tabelaRoteamento(self, tabelaRoteamento):
        self.__tabelaRoteamento = tabelaRoteamento

    def conectarComputador(self, porta, computador):
        if self.__tabelaRoteamento[porta - 1][0] == None:
            self.__tabelaRoteamento[porta - 1][0] = porta
            self.__tabelaRoteamento[porta - 1][1] = computador.macAddress
