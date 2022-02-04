import math
class IMCException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

def imcCalculo(peso, altura):
    try:
        imc = round(peso / math.pow(altura, 2), 2)
    except ZeroDivisionError:
        print('Não é permitido o valor zero para o cálculo de IMC')
    else:     
        if imc < 18.5:
            categoria = 'Peso abaixo do normal' 
        elif imc > 18.5 and imc < 24.9:
            categoria = 'Peso normal'
        elif imc > 24.9 and imc <= 29.9:
            categoria = 'Pré-obesidade'
        elif imc > 29.9 and imc < 34.9:
            categoria = 'Obesidade grau I'
        elif imc > 34.9 and imc <= 39.9:
            categoria = 'Obesidade grau II'
        else:
            categoria = 'Obesidade grau III'
    
        return imc, categoria
    return None, None
    
spa = []
while(True):
    print('--------------------')
    print('Calculadora IMC')
    print('--------------------')
    print('(c) Calcular IMC')
    print('(s) Sair')
    print('---------------------')
    opcao = input('opcao: ')
    opcao = opcao.lower()

    while opcao.lower() != 'c' and opcao.lower() != 's':
        print('Opção inválida, tente novamente')
        opcao = input('opcao: ')
        opcao = opcao.lower()

    if opcao == 'c': ### calcular IMC
        peso = 1
        print('OBS: Se quiser ir para o menu principal digite zero no pedido do peso')
        while peso != 0:
            try:
                peso = int(input('Digite o peso: '))
                if peso == 0:
                    break
            except ValueError:
                print('Dado inserido de maneira errônea, o valor deve ser do tipo inteiro, tente Novamente')
            else:    
                try:
                    altura = float(input('Digite a altura: ').replace(',','.'))
                except ValueError:
                    print('Dado inserido de maneira errônea, tente novamente')
                    #except TypeError:
                    #   print('O valor para altura deve ser de ponto flutuante')
                else:
                    try:
                        imc, categoria = imcCalculo(peso, altura)
                        if imc != None and categoria != None: 
                            print('O seu imc é {} e você está na categoria {}'.format(imc, categoria))
                        if categoria == 'Obesidade grau III':
                            raise IMCException('Você deve procurar um médico imediatamente')
                            #print(IMCException.mensagem)
                    except IMCException as msg:
                        print(msg)
                    spa.append(imc)
    elif opcao == 's':
         break

