numbersList = []

#This loop will repeat the data input and insert the number type to list
for i in range(6):
    number = int(input('Type the ' + str(i + 1) + '° number: '))
    numbersList.append(number)

for j in numbersList:
    if j > (sum(numbersList) / len(numbersList)):
        print(j, end = ' ')
