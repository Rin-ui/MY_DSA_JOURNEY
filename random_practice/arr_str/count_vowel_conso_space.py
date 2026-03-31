s = input()
s.lower()
vowel = 0
consonant = 0
spaces = 0
for i in s:
    if i in ['a','e','i','o','u']:
        vowel +=1
    elif i == " ":
        spaces +=1
    else:
        consonant +=1
print(vowel , consonant, spaces)
