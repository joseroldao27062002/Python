length = int(input())
velocitiesArray = []

velocity = input().split()

for i in range(length):
   velocitiesArray.append(int(velocity[i]))

for j in range(length - 1):
    if velocitiesArray[j] > velocitiesArray[j + 1]:
        print(velocitiesArray.index(velocitiesArray[j + 1]) + 1)
        break

if velocitiesArray[j] <= velocitiesArray[j + 1]:
    print(0)
