import math
n = int(input())

hours = math.trunc(n / 3600)

minutes = math.trunc(n % 3600 / 60)

seconds = math.trunc(n - hours * 3600 - minutes * 60)

print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
