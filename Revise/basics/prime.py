x = int(input("enter a number: "))
if x < 2:
    print("not prime")
for i in range(2, x):
    if x % i ==0:
        print("not prime")
        break
else:
    print("prime")
