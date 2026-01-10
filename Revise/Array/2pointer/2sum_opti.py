# 2 sum optimal
arr = list(map(int, input().split()))
target = int(input("enter target: "))

arr.sort()   # required for two-pointer approach

left = 0
right = len(arr) - 1

while left < right:
    if arr[left] + arr[right] < target:
        left += 1
    elif arr[left] + arr[right] > target:
        right -= 1
    else:
        print(f'[{left},{right}]')
        break
