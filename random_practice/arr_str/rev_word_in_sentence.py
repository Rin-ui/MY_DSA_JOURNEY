s = input()
words = s.split()
result = " "
for i in words:
    result += i[::-1] + " "
print(result.strip())
    
