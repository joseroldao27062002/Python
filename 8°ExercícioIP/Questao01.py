def divisores(numero):
    listaDivisores = []
    divisor = 1

    while numero >= divisor:
        if numero % divisor == 0:
            listaDivisores.append(divisor)
        divisor += 1

    for i in listaDivisores:
        print(i, end = ' ')

numero = int(input('Digite o número desejado: '))
divisores(numero)
