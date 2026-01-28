n = int(input("enter money amount: "))
choice = list(map(int, input().split()))
list = []
while n > 0:
    for c in range(len(choice)):
        if n//choice[c] == 0:
            continue
        else:
            d = n // choice[c]
            n = n % choice[c]
            for count in range(d):
                list.append(choice[c])
print(list)
