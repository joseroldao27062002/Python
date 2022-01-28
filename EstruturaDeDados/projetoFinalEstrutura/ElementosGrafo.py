class Aresta():
        def __init__(self, v, w):
                self.__v = v 
                self.__w = w
	
        @property
        def v(self) -> 'Vertice':
                return self.__v

        @v.setter
        def v(self, v: 'Vertice'):
                self.__v = v

        @property
        def w(self) -> 'Vertice':
                return self.__w
	
        @w.setter
        def w(self, w: 'Vertice'):
                self.__w = w

        def __str__(self):
                return f'{self.__v},{self.__w}'


class Vertice():
        def __init__(self, dado):
                self.__dado = dado
                self.__adj = list()
	
        def addAdj(self, edge: Aresta):
                self.__adj.append(edge)
	
        @property
        def dado(self):
                return self.__dado
	
        @dado.setter
        def dado(self, dado):
                self.__dado = dado
	
        @property
        def adj(self):
                return self.__adj
	

        def __str__(self):
                return self.__dado
