arr = list(map(int,input().split()))
k = int(input('enter number: '))
arr.sort()
left = 0
right = len(arr) -1
cost = 0
while left < right:
    cost += arr[left]
    for i in range(k):
        right -=1
    left +=1
print(cost)
