listOfSpecialcharacters = [chr(i) for i in range(32, 48)]
phrase = input()
Specialcharacters = 0

for i in range(len(phrase)):
    if phrase[i] in listOfSpecialcharacters:
        Specialcharacters += 1
    
print(Specialcharacters)


