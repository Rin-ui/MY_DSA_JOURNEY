n = int(input("enter a number: "))
list1 = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        print(i, end=" ")
        if i != n // i:
            list1.append(n // i)

for x in reversed(list1):
    print(x, end=" ")
