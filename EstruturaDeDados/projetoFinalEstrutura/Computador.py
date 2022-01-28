from Dispositivo import Dispositivo
from TabelaHash import TabelaHash 
class Computador(Dispositivo):
    def __init__(self, nome, ipAddress, macAddress):
        super().__init__(ipAddress, macAddress)
        self.__nome = nome
        self.__tabelaArp = TabelaHash()

    #Métodos getter
    @property
    def nome(self):
        return self.__nome
    
    @property
    def tabelaArp(self):
        return self.__tabelaArp

    #Métodos setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tabelaArp.setter
    def tabelaArp(self, tabelaArp):
        self.__tabelaArp = tabelaArp

    def enviarMensagem(self, ipAddress):
        pass


