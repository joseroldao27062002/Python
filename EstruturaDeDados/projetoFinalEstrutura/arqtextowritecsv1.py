# Escrita no modo 'w', mapeamento de um list para um arquivo texto
arq = open('arquivo1.csv','w')

pcontas = [('100','caixa','S',0.0),('101','BB','S',100.0),('102','Bradesco','A',150.0)]

for conta in pcontas:
    cont = 0
    for e in conta:
        cont += 1
        arq.write(str(e) )
        if cont < len(conta):
            arq.write(';')
        
    arq.write('\n')
    

print('Arquivo gravado com sucesso!')
arq.close()
