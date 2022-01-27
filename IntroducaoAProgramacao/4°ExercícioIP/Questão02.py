firstGrade = float(input())
#Making the data validation
while firstGrade < 0 or firstGrade > 10:
    print('Nota invalida')
    firstGrade = float(input())

#Making the data validation
secondGrade = float(input())
while secondGrade < 0 or secondGrade > 10:
    print('Nota invalida')
    secondGrade = float(input())

average = (firstGrade + secondGrade) / 2.0
print('media =', average)
