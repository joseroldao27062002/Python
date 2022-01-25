operation = input()
array = []

for i in range(12):
    array.append([0]*12)

for j in range(0, 12):
    for k in range(12):
        number = float(input())
        array[j][k] = number

soma = 0
end = 0
for l in range(1, 12):
    end += 1
    for m in range(0, end):
        soma += array[l][m]

if operation == 'S':
    print('{:.1f}'.format(soma))
elif operation == 'M':
     print('{:.1f}'.format(soma / 66))
