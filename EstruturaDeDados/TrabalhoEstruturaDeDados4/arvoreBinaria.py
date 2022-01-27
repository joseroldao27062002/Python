class No:
    def __init__(self, carga, esquerda = None, direita = None):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita

class ArvoreBinaria:
    def __init__(self, raiz):
        self.raiz = raiz
             
    def inOrdem(self, no, raiz):
        if no is None:
            no = self.raiz
        if no.esquerda is not None:
            print('(', end='')
            self.inOrdem(no.esquerda, no)
        if no.carga is not None:
            print(no.carga, end='')
        if no.direita is not None:
            self.inOrdem(no.direita, no)
            print(')', end='')          
    
    def efetuarOperacao(self):
        vetorStored = []
        vetorStored = armazenar(self, self.raiz, self.raiz, vetorStored)
        elementosVerificados = []
        expressao = ""
        
        for i in range(len(vetorStored) + 4):
            if vetorStored[i] == '12' and '12' not in elementosVerificados:
                vetorStored.insert(0, '(')
                elementosVerificados.append('12') 
            elif vetorStored[i] == '+' and '+' not in elementosVerificados:
                vetorStored.insert(3, '(')
                elementosVerificados.append('+') 
            elif vetorStored[i] == '*' and '*' not in elementosVerificados:
                vetorStored.insert(6,'((')
                elementosVerificados.append('*') 
            elif vetorStored[i] == '2' and '2' not in elementosVerificados:
                vetorStored.insert(10, ')')
                elementosVerificados.append('2') 
            elif vetorStored[i] == '7' and '7':
                vetorStored.append(')))')
                elementosVerificados.append('7') 

        print(vetorStored) 
        for j in vetorStored:
            expressao += j

        #print(expressao)
        
        return eval(expressao)

    def calcularAltura(self, raiz):
        alturaDireita = 0
        alturaEsquerda = 0

        if raiz.esquerda is not None:
            alturaEsquerda = self.calcularAltura(raiz.esquerda)
        if raiz.direita is not None:
            alturaDireita = self.calcularAltura(raiz.direita)
        if alturaDireita < alturaEsquerda:
            return alturaEsquerda + 1
        else:
            return alturaDireita + 1

    #def verificarSimetria(self, raiz1, raiz2 = None):
     #   if self.calcularAltura(raiz1) - self.calcularAltura(raiz2) == 0:
      #      if raiz1.esquerda is not None and raiz2.esquerda is not None: 
       #         verificarSimetria(raiz1.esquerda, raiz2.direita)
            
        #else:
         #   return False

    def verificarArvoreAVL(self, raiz1, raiz2):
        fatorBalanceamento = self.calcularAltura(raiz1) - self.calcularAltura(raiz2)
        if fatorBalanceamento == 1 or fatorBalanceamento == 0 or fatorBalanceamento == -1:
            return True
        return False


def verificarSimetria(arvore1, arvore2):
    if arvore1.esquerda is not None and arvore2.direita is not None:
        if (arvore1.esquerda.carga == arvore2.direita.carga) and (arvore1.direita.carga == arvore2.esquerda.carga):
            return True
    return False

def armazenar(arvore, no, raiz, vetor):    
    if no is None:
        no = arvore.raiz
    if no.esquerda is not None:
        armazenar(arvore, no.esquerda, no, vetor)
    if no.carga is not None:
        vetor.append(no.carga)
    if no.direita is not None:
        armazenar(arvore, no.direita, no, vetor)
    return vetor

def comparar(arvore1, no1, raiz1, vetor1, arvore2, no2, raiz2, vetor2):
    if armazenar(arvore1, no1, raiz1, vetor1) == armazenar(arvore2, no1, raiz2, vetor2):
        return True
    else:
        return False

#Programa principal
no1 = No('12')
no3 = No('10')
no7 = No('20')
no8 = No('2')
no5 = No('/', no7, no8)
no6 = No('7')
no4 = No('-', no5, no6)
no2 = No('*', no3, no4)
raiz = No('+', no1, no2)
arvoreBinaria = ArvoreBinaria(raiz)

print(arvoreBinaria.verificarArvoreAVL(no1, no2))

arvoreBinaria.inOrdem(raiz, raiz)
print()
vetor1 = []

no1 = No('12')
no3 = No('10')
no7 = No('20')
no8 = No('2')
no5 = No('/', no7, no8)
no6 = No('7')
no4 = No('-', no5, no6)
no2 = No('*', no3, no4)
raiz2 = No('+', no1, no2)

vetor2 = []
arvoreBinaria2 = ArvoreBinaria(raiz2)

if arvoreBinaria2.verificarArvoreAVL(no1, no2) == True:
    print('A árvore é uma árvore AVL')
else:
    print('A árvore não é uma árvore AVL')

print(comparar(arvoreBinaria, raiz, raiz, vetor1, arvoreBinaria2, raiz2, raiz2, vetor2))

print(arvoreBinaria.efetuarOperacao())

print(arvoreBinaria.calcularAltura(raiz))

no6 = No('3') 
no7 = No('4')
no5 = No('2', no6, no7)
no4 = No('3')
no3 = No('4')
no1 = No('2', no3, no4)
no2 = No('2', no6, no7)
raiz3 = No('1', no1, no2)

arvoreBinaria3 = ArvoreBinaria(raiz3)
print(verificarSimetria(raiz3.esquerda, raiz3.direita))

print(arvoreBinaria3.verificarArvoreAVL(no1, no2))



