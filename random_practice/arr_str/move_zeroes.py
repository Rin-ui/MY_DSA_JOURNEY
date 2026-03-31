n = int(input())
arr = list(map(int,input().split()))
count = 0
new_arr = []
for i in range(len(arr)):
    if arr[i] ==0:
        count +=1
        continue
    else:
        new_arr.append(arr[i])
for i in range(count):
    new_arr.append(0)
print(*new_arr)
        
