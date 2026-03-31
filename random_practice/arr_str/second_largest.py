n = int(input())
arr = list(map(int,input().split()))
largest = float('-inf')
second = float('-inf')
for i in range(len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] != largest and arr[i] > second:
        second = arr[i]
print(second)
