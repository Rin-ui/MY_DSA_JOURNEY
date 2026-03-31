string = input()
s= set()
result = ""
for i in range(len(string)):
    if string[i] not in s:
        s.add(string[i])
        result += string[i]
    
print(result)
