from Grafo import Grafo

g = Grafo()
print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
v1 = g.addVertice('alex')
v2 = g.addVertice('diego')
print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
g.addAresta(v1,v2,10)
v3 = g.addVertice('damires')
g.addAresta(v2,v3,15)
g.addAresta(v1,v3,25)
print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

print(g)
