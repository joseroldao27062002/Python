word  = input()
listOfNumbers = [str(i) for i in range(10)]
isNumber = True

for j in word:
    if j not in listOfNumbers:
        isNumber = False
        break

if isNumber == True:
    print('Sim')
else:
    print('Não')
