age = int(input())
quantityOfAges = 0
sumOfAges = 0

while age >= 0:
    quantityOfAges += 1
    sumOfAges += age
    age = int(input())
print('{:.2f}'.format(sumOfAges / quantityOfAges))
    
