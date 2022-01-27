def distintos(lista):
    saoDistintos = True
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                saoDistintos = False
        if saoDistintos == False:
            break
    return saoDistintos

lista = []
tamanhoLista = int(input('Digite o tamanho desejado da sua lista: '))

for i in range(0, tamanhoLista):
    elemento = int(input('Digte o número desejado: '))
    lista.append(elemento)

print(distintos(lista))

        
        
    
            
                
