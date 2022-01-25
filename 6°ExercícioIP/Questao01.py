line = int(input())
operation = input()
array = []

for i in range(12):
    array.append([0]*12)

for j in range(12):
    for k in range(12):
        number = float(input())
        array[j][k] = number

if operation == 'S':
    print('{:.1f}'.format(sum(array[line])))
elif operation == 'M':
     print('{:.1f}'.format(sum(array[line] / 12)))

for c in range(12):
    for i in range(12):
        print(array[c][i], end = ' ')
    print()

