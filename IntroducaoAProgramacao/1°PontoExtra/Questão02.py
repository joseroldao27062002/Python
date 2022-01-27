numbersList = []

#This loop will repeat the data input and insert the number type to list
for i in range(6):
    number = int(input('Type the ' + str(i + 1) + '° number: '))
    numbersList.append(number)

#This loop will access the element by their index and print them on reverse order
for j in range(len(numbersList) - 1, -1, -1):
    print(numbersList[j], end = ' ')
