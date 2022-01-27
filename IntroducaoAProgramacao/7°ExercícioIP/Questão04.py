listOfNumbers = [str(i) for i in range(10)]
isIntegerNumber = False

while isIntegerNumber == False:
    number = input()
    for j in range(len(number)):
        if number[j] not in listOfNumbers:
            isIntegerNumber = False
            break
    if j == (len(number) - 1):
        isIntegerNumber = True

print(number)
