phrase = input()
listOfVowels = ['a','e','i','o','u']
vowels = 0

for c in phrase:
    if c.lower() in listOfVowels:
        vowels += 1

print(vowels)
