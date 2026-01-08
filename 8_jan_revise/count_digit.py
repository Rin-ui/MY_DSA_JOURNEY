n = int(input("enter a number: "))
count = 0
rev = 0
while n > 0:
    rev = n % 10
    count +=1
    n = n//10

print(count)
