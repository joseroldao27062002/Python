import os
from time import sleep
class Bomba:
    def __init__(self, combustivel, totalApagar = 0, litros = 0):
        self._totalApagar = totalApagar
        self._litros = litros
        self._combustivel = combustivel

    def reajustarPreco(self, combustivel, nomeCombustivel, novoPreco):
        if self.nomeCombustivel == combustivel.tipo:
            self.combustivel.precoPorLitro = novoPreco

    @property 
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, combustivel):
        self._combustivel = combustivel

    @property
    def totalApagar(self):
        return self._totalApagar

    @totalApagar.setter
    def totalApagar(self, totalApagar):
        self._totalApagar = totalApagar

    @property
    def litros(self):
        return self._litros
    
    @litros.setter
    def litros(self, litros):
        self._litros = litros
    
    def zerarBomba(self):
        self.litros = 0
        self.totalApagar = 0

    def abastecer(self, precoDesejado, combustivel):
        litro = 0
        preco = 0

        while preco < precoDesejado:
                preco += 0.1
                print('Total a pagar R$' + str(round(preco, 2)))
                os.system('clear')
                sleep(0.01)
                #print('Litros abastecidos ' + str(round(litro, 2)))
        #self.totalApagar = preco
        print('Total a pagar: R$', self.totalApagar)
        print(self)
        print('Litros abastecidos: ' + str(round(self.litros, 2)) + 'L')
        self.zerarBomba()
        print('Veículo abastecido!')

    def __str__(self):
        return "Tipo do Combustivel: " + str(self.combustivel.tipo) + "\nPreço por litro: " + str(self.combustivel.precoPorLitro)

        
        

