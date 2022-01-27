length = int(input())
array = []

number = input().split()

for j in range(length):
   array.append(int(number[j]))

print('Menor valor: ' + str(min(array)))
print('Posicao: ' + str(array.index(min(array))))
