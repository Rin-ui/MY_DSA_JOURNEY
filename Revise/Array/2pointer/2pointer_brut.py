# 2 sum brute force
arr = list(map(int, input().split()))
target = int(input("enter target: "))
for i in range(len(arr)):
    for j in range(i +1 , len(arr)):
        if arr[i] + arr[j] == target:
            print(f'[{i},{j}]')
