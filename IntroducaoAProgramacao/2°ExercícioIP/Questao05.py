firstNumber, secondNumber = input().split()

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

if (secondNumber // firstNumber) * firstNumber == secondNumber:
    print('São múltiplos')
else:
    print('Não são múltiplos')
