n = int(input())
arr = list(map(int,input().split()))
summ = 0
repeat = 0
missing = 0
store = {}
for i in arr:
    if i not in store:
        store[i] = 1
    else:
        repeat = i
for i in arr:
    summ += i
num = n * (n + 1)//2
missing = num - (summ - repeat)
print(missing , repeat)
