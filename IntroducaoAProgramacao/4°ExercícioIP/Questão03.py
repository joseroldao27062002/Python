#Declaration of variables
interGoals, gremioGoals = input().split()
gremioGoals = int(gremioGoals)
interGoals = int(interGoals)

quantityOfGames = 1
gremioVictory = 0
interVictory = 0
draws = 0

#Decision block
if gremioGoals > interGoals:
    gremioVictory += 1
elif gremioGoals < interGoals:
    interVictory += 1
else:
    draws += 1

print('Novo grenal (1-sim 2-nao)')

opcao = int(input())

#Loop
while opcao == 1:
    interGoals, gremioGoals = input().split()
    gremioGoals = int(gremioGoals)
    interGoals = int(interGoals)

    if gremioGoals > interGoals:
        gremioVictory += 1
    elif gremioGoals < interGoals:
        interVictory += 1
    else:
        draws += 1


    print('Novo grenal (1-sim 2-nao)')

    opcao = int(input())

    quantityOfGames += 1
        
print(str(quantityOfGames) + ' grenais')
print('Inter: ' + str(interVictory)+ '\nGremio: ' + str(gremioVictory)+ '\nEmpates: ' + str(draws))

if gremioVictory > interVictory:
    print('Gremio venceu mais')
elif interVictory > gremioVictory:
    print('Inter venceu mais')
