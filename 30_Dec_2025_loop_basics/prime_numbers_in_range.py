# find prime number in a range
start = int(input("enter starting point: "))
end = int(input("enter ending point: "))

for i in range(start, end + 1):
    if i < 2:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
