n = int(input("enter a number: "))
temp = n
original = n
count = 0
num = 0

# count digits
while n > 0:
    count = count + 1
    n = n // 10

# calculate armstrong sum
while temp > 0:
    digit = temp % 10
    num = num + digit ** count
    temp = temp // 10

if original == num:
    print(True)
else:
    print(False)
