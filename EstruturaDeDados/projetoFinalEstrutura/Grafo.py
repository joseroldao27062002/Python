from ElementosGrafo import *
class Grafo():
	def __init__(self):
		self.__vertices = list()
		self.__arestas = list()

	def addVertice(self, vertice)->Vertice:
		self.__vertices.append(vertice)
	
	def addAresta(self, v: Vertice, w: Vertice)->Aresta:
		e = Aresta(v, w)
		v.addAdj(e)
		self.__arestas.append(e)

	def __str__(self):
		r = ''
		for u in self.__vertices:
			if len(u.adj) == 0:
				continue
			r += (str(u.dado.ipAddress) + ' <-> ')
			for e  in u.adj:
				v: Vertice = e.w
				r += v.dado.ipAddress + ', '
			r += '\n'
		return r

	def getNumVertices(self):
		return len(self.__vertices)

	def getNumArestas(self):
		return len(self.__arestas)	



