a = []
for i in range(100):
    number = float(input())
    a.append(number)

for j in range(len(a)):
    if a[j] < 100:
        print('A[{}] = {}'.format(j, a[j]))
