# abertura no modo r, função readline(), leitura de arquivo CSV, mapeando para um list

def lerArquivo(arquivo):
    arq = open(arquivo,'r')

    dados = []

    linha = arq.readline()
    while (linha != ''):    
        tokens = linha.split(';') # tokens é um list
        tupla = ()
        for s in tokens:
            #print(s)
            tupla = tupla + (s,)
        #print(tupla)
        dados.append(tupla)
        linha = arq.readline()

    #print('Dados: ',dados)
    return dados
    arq.close()

lerArquivo('computadores.csv')
