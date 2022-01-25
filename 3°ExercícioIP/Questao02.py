pairNumbers = 0
oddNumbers = 0
positivesNumbers = 0
negativesNumbers = 0

for c in range(0, 5, 1):
    number = int(input())
    if number > 0:
        positivesNumbers += 1
    if number < 0:
        negativesNumbers += 1
    if number % 2 == 0:
        pairNumbers += 1
    if number % 2 == 1:
        oddNumbers += 1

print(str(pairNumbers) + ' valor(es) par(es)\n' + str(oddNumbers) + ' valor(es) impar(es)\n'
        + str(positivesNumbers) + ' valor(es) positivo(s)\n' + str(negativesNumbers) + ' valor(es) negativo(s)') 
        