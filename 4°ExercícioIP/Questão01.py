firstNumber, secondNumber = input().split()
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

while firstNumber != secondNumber:
    if firstNumber < secondNumber:
        print('Crescente')
    elif secondNumber < firstNumber:
        print('Decrescente')

    firstNumber, secondNumber = input().split()
    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)

    
