distinctNumbers = 0
listDistinctNumbers = []

while distinctNumbers < 6:
    number = int(input('Type a number: '))
    if number not in listDistinctNumbers:
        listDistinctNumbers.append(number)
        distinctNumbers += 1

for i in listDistinctNumbers:
    print(i, end = ' ')
