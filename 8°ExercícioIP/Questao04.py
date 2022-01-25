def especial(st):
    listaDeCaracteresEspeciais = [chr(i) for i in range(32, 48)]
    caracteresEspeciais = 0

    for i in range(len(st)):
        if st[i] in listaDeCaracteresEspeciais:
            caracteresEspeciais += 1
    return caracteresEspeciais

palavra = input('Digite a palavra desejada: ')
print(especial(palavra))
