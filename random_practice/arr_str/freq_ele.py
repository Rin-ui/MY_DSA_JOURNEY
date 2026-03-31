n = int(input())
arr = list(map(int,input().split()))
store = {}
for i in range(len(arr)):
    if arr[i] not in store:
        store[arr[i]] = 1
    else:
        store[arr[i]] +=1
for key, val in store.items():
    print(key,val)
