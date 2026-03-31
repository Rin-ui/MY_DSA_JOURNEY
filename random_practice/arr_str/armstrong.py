n = int(input())
temp = n
val = n
p = 0
count = 0
while n > 0:
    count +=1
    n = n // 10
while temp > 0:
    rem = temp % 10
    p += rem ** count
    temp = temp // 10
if p == val:
    print("armstrong")
else:
    print("not armstrong")
    
