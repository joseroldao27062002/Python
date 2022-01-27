number = int(input())

while number != 0:
    for c in range(1, number, +1):
        print(c, end = ' ')
    print(number, end = '')
    number = int(input())
