quantityOfExperiments = int(input())
rabbits = 0
froags = 0
rats = 0

for c in range(quantityOfExperiments):
    quantityOfAnimals, typeOfAnimal = input().split()
    #Converting the string variable to integer variable
    quantityOfAnimals = int(quantityOfAnimals)
    typeOfAnimal = str(typeOfAnimal)

    if typeOfAnimal == "C":
        rabbits += quantityOfAnimals
    elif typeOfAnimal == "S":
        froags += quantityOfAnimals
    elif typeOfAnimal == "R":
        rats += quantityOfAnimals

#Calculating the percents
rabbitsPercent = rabbits * 100 / (rabbits + froags + rats)
ratsPercent = rats * 100 / (rabbits + froags + rats)
frogsPercent = froags * 100 / (rabbits + froags + rats)

print('Total: ' + str(rabbits + froags + rats) + ' cobaias')
print('Total de coelhos: ',rabbits)
print('Total de ratos: ',rats)
print('Total de sapos: ',froags)
print('Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %'.format(rabbitsPercent,ratsPercent,frogsPercent))

    
