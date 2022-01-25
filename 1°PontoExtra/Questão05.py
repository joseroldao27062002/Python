pairs = 0

pairNumbers = []
while pairs < 6:
    number = int(input('Type a number: '))
    if number % 2 == 0:
        pairNumbers.append(number)
        pairs += 1

for i in pairNumbers:
    print(i, end = ' ')
