startTime, endTime = input().split()
#Converting the strings variables to integers variables
startTime = int(startTime)
endTime = int(endTime)

if startTime > endTime or startTime == endTime:
    duration = 24 - startTime + endTime
else:
    duration = endTime - startTime
print('O JOGO DUROU ' + str(duration) + ' HORA(S)')
