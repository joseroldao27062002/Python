# abertura de arquivo, para gravação, no modo 'a'
arq = open('arquivo1.txt','a')
while(True):
    s = input('Digite uma string: ')
    if s == '':
        break
    arq.write(s + '\n')
arq.close()
