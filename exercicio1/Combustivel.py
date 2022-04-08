class Combustivel:
    def __init__(self, tipo, precoPorLitro):
        self._tipo = tipo
        self._precoPorLitro = precoPorLitro

    #Métodos acessores e modificadores do atributo tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    #Métodos acessores e modificadores do atributo precoPorLitro
    @property
    def precoPorLitro(self):
        return self._precoPorLitro

    @precoPorLitro.setter
    def precoPorLitro(self, precoPorLitro):
        if precoPorLitro > 0:
            self._precoPorLitro = precoPorLitro

