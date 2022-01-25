import math
#This is going to allow the data input in only one line
a, b, c = input().split()
#Converting the strings variables to floaters variables
a = float(a)
b = float(b)
c = float(c)

delta = math.pow(b, 2) - 4 * a * c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
