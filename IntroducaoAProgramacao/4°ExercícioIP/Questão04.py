typeOfFuel = int(input())
alcohol = 0
gasoline = 0
diesel = 0

while typeOfFuel != 4:
    if typeOfFuel == 1:
        alcohol += 1
    elif typeOfFuel == 2:
        gasoline += 1
    elif typeOfFuel == 3:
        diesel += 1
    typeOfFuel = int(input())
    if typeOfFuel < 1 or typeOfFuel > 4:
        typeOfFuel = int(input())

print('MUITO OBRIGADO')
print('Alcool: ' + str(alcohol) + '\nGasolina: ' + str(gasoline) + '\nDiesel: ' + str(diesel))
