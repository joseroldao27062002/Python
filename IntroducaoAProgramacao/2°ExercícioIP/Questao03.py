code,quantity = input().split()
price = 0

#Converting the string variables to integers variables
code = int(code)
quantity = int(quantity)


if (code == 1):
    price = 4.0
elif (code == 2):
    price = 4.5
elif (code == 3):
    price = 5.0
elif (code == 4):
    price = 2.0
elif (code == 5):
    price = 1.5

totalPrice = quantity * price

print('Total: R${:.2f}'.format(totalPrice))
