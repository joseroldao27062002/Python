sum = 0
positivesNumbers = 0
for c in range(0, 6, 1):
    number = float(input())
    if number > 0:
        sum += number
        positivesNumbers += 1
average = sum / positivesNumbers

print(str(positivesNumbers) + ' valores positivos')
print('{:.1f}'.format(average))