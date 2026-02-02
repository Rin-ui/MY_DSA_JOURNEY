x = int(input("enter a number: "))
sign = 1
rev = 0
digit = 0
if x < 0:
    sign = -1
    x = -x
while x > 0:
    digit = x % 10
    # overflow check before updating rev
    if rev > (2**31 - 1) // 10:
        print(0)
    rev = rev*10 + digit
    x = x//10
    
print(sign * rev)
