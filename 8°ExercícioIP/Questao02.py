def primo(numero):
    ehPrimo = False
    qtdDivisores = 0
    for i in range(1, numero +1):
        if numero % i == 0:
            qtdDivisores += 1

    if qtdDivisores == 2:
        ehPrimo = True

    return ehPrimo

numero = int(input('Dgite o número desejado: '))
print(primo(numero))
