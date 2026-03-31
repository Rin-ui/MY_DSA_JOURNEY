n=int(input())
temp = n 
digit = 0
rem = 0
if n < 0:
    print("false")
while n > 0:
    rem = n % 10
    digit = digit * 10 + rem 
    n = n // 10
if temp == digit:
    print("true")
else:
    print("false")
