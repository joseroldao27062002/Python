numbersList = []

#This loop will repeat the data input and insert the number type to list
for i in range(10):
    number = int(input('Type the ' + str(i + 1) + '° number: '))
    numbersList.append(number)

for j in numbersList:
    if j > numbersList[len(numbersList) - 1]:
        print(j, end = ' ')
