highestNumber = 0
highestNumberPosition = 0

for c in range(0, 10, +1):
    number = int(input())
    if number > highestNumber:
        highestNumber = number
        highestNumberPosition = c + 1
print(highestNumber)
print(highestNumberPosition)
