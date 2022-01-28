import arqtextoreadcsv1
from ElementosGrafo import *
from Grafo import *
from Computador import Computador
from Switch import Switch
from TabelaHash import TabelaHash

arqComputadores = arqtextoreadcsv1.lerArquivo('computadores.csv')
arqSwitchs = arqtextoreadcsv1.lerArquivo('switchs.csv')

#Criação dos computadores
c1 = Vertice(Computador(arqComputadores[0][1], arqComputadores[0][0], arqComputadores[0][2]))
c2 = Vertice(Computador(arqComputadores[1][1], arqComputadores[1][0], arqComputadores[1][2]))
c3 = Vertice(Computador(arqComputadores[2][1], arqComputadores[2][0], arqComputadores[2][2]))
c4 = Vertice(Computador(arqComputadores[3][1], arqComputadores[3][0], arqComputadores[3][2]))

#Criação dos switches
s1 = Vertice(Switch(arqSwitchs[0][0], arqSwitchs[0][1], 24))
s2 = Vertice(Switch(arqSwitchs[1][0], arqSwitchs[1][1], 24))

#print(s2.dado.macAddress)
#Criação das arestas
aresta1 = Aresta(c1, s1)
aresta2 = Aresta(c2, s1)
aresta3 = Aresta(c3, s2)
aresta4 = Aresta(c4, s2)
aresta5 = Aresta(s1, s2)

rede = Grafo()

#adicionando os vértices no grafo
rede.addVertice(c1)
rede.addVertice(c2)
rede.addVertice(c3)
rede.addVertice(c4)
rede.addVertice(s1)
rede.addVertice(s2)

#adicionando as arestas no grafo
rede.addAresta(c1, s1)
rede.addAresta(c2, s1)
rede.addAresta(c3, s2)
rede.addAresta(c4, s2)
rede.addAresta(s1, s2) 

s1.dado.conectarComputador(1, c1.dado)
s1.dado.conectarComputador(2, c2.dado)
s1.dado.conectarComputador(24, c3.dado)
print('*** Grafo ***')
print(rede)
print('*** Tabela de roteamento do switch1')
print(s1.dado.tabelaRoteamento)

print('*** Tabela Arp ***')
c1.dado.tabelaArp.adicionarItem(c2.dado.ipAddress, c2.dado.macAddress)
print(c1.dado.tabelaArp.vetor)
