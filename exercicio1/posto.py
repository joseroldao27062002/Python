from Combustivel import Combustivel
from Bomba import Bomba 
print('*** Posto Boa Viagem ***')

combustivel1 = Combustivel('Gasolina', 6.80)
combustivel2 = Combustivel('Alcool', 5.70)
opcaoOperacao = 3

while opcaoOperacao != 0:
    print('*** Opções ***\n**1-Reajustar preço**\n**2-Abastecer**\n**0-sair')

    opcaoOperacao = int(input('Digite a opção de operação: '))
    if opcaoOperacao == 1:
        print('*** Opções ***\n**1-Gasolina**\n**2-Álcool**')
        opcao = int(input('Digite a opção desejada: '))
        novoPreco = float(input('Digite o novo preco de reajuste: '))
        
        if opcao == 1:
            nomeCombustivel = "Gasolina"
            combustivel1.precoPorLitro = novoPreco
            print('**Preço reajustado **\nNome do combustível: ' + nomeCombustivel + '\nNovoPreco: ' + str(round(combustivel1.precoPorLitro, 2)))
        elif opcao == 2:
            nomeCombustivel = "Álcool"
            combustivel2.precoPorLitro = novoPreco
            print('**Preço reajustado **\nNome do combustível: ' + nomeCombustivel + '\nNovoPreco: ' + str(round(combustivel2.precoPorLitro, 2)))

    elif opcaoOperacao == 2:
        print('*** Seja bem vindo ***')
        print('*** Opções ***\n**1-Gasolina - ' + str(round(combustivel1.precoPorLitro, 2)) + '**\n**2-Álcool - ' + str(round(combustivel2.precoPorLitro, 2)) + '**')

        opcao = int(input('Digite a opção desejada: '))

        while opcao != 1 and opcao != 2:
            print('Opções não disponíveis, por favor, digite novamente')
            opcao = int(input('Digite a opcao desejada: '))
 
        if opcao == 1:
            totalAPagar = float(input('Quanto você deseja de ' + str(combustivel1.tipo) + ': '))
            bomba = Bomba(combustivel1, totalAPagar, totalAPagar / combustivel1.precoPorLitro)
            bomba.abastecer(totalAPagar, combustivel1);
        elif opcao == 2:
            totalAPagar = float(input('Quanto você deseja de ' + str(combustivel2.tipo) + ': '))
            bomba = Bomba(combustivel2, totalAPagar, totalAPagar / combustivel2.precoPorLitro)
            bomba.abastecer(totalAPagar, combustivel2);
