def menor(lista):
    menorElemento = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < menorElemento:
            menorElemento = lista[i]

    return menorElemento

lista = []
tamanhoLista = int(input('Digite o tamanho desejado da sua lista: '))

for i in range(0, tamanhoLista):
    elemento = int(input('Digte o número desejado: '))
    lista.append(elemento)

print(menor(lista))
