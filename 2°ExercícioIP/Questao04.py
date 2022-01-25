firstNumber, secondNumber, thirdNumber = input().split()

#Converting the strings variables to integers variables
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)
thirdNumber = int(thirdNumber)

integerList = []

if firstNumber < secondNumber and firstNumber < thirdNumber:
    integerList.append(firstNumber)
    if secondNumber < thirdNumber:
        integerList.append(secondNumber)
        integerList.append(thirdNumber)
    else:
        integerList.append(thirdNumber)
        integerList.append(secondNumber)
elif secondNumber < firstNumber and secondNumber < thirdNumber:
    integerList.append(secondNumber)
    if firstNumber < thirdNumber:
        integerList.append(firstNumber)
        integerList.append(thirdNumber)
    else:
        integerList.append(thirdNumber)
        integerList.append(firstNumber)
elif thirdNumber < firstNumber and thirdNumber < secondNumber:
    integerList.append(thirdNumber)
    if secondNumber < firstNumber:
        integerList.append(secondNumber)
        integerList.append(firstNumber)
    else:
        integerList.append(firstNumber)
        integerList.append(secondNumber)

for c in integerList:
    print(c)
print()

print(firstNumber, secondNumber, thirdNumber, sep = '\n')
        
