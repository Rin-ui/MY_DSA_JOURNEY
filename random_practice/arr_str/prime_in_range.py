high = int(input())
for i in range(high + 1):
    if i < 2:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i , end = " ")
