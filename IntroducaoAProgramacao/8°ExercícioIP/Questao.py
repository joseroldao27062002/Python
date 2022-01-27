def divisores(n):
    listaDivisores = []
    divisor = 1

    while n >= divisor:
        if n % divisor == 0:
            listaDivisores.append(divisor)
        divisor += 1

    for i in listaDivisores:
        print(i, end = ' ')

def primo(n):
    ehPrimo = False
    qtdDivisores = 0
    for i in range(1, n +1):
        if n % i == 0:
            qtdDivisores += 1

    if qtdDivisores == 2:
        ehPrimo = True

    return ehPrimo

def menor(lista):
    menorElemento = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < menorElemento:
            menorElemento = lista[i]

    return menorElemento

def especial(st):
    listaDeCaracteresEspeciais = [chr(i) for i in range(32, 48)]
    caracteresEspeciais = 0

    for i in range(len(st)):
        if st[i] in listaDeCaracteresEspeciais:
            caracteresEspeciais += 1
    return caracteresEspeciais

def distintos(lista):
    saoDistintos = True
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                saoDistintos = False
        if saoDistintos == False:
            break
    return saoDistintos

#Questao01 e  Questao02
numero = int(input('Digite o número desejado: '))
divisores(numero)
print()
print(primo(numero))

#Questao03 e Questão05
lista = []
tamanhoLista = int(input('Digite o tamanho desejado da sua lista: '))

for i in range(0, tamanhoLista):
    elemento = int(input('Digte o número desejado: '))
    lista.append(elemento)

print(menor(lista))
print(distintos(lista))

#Questao04
palavra = input('Digite a palavra desejada: ')
print(especial(palavra))

