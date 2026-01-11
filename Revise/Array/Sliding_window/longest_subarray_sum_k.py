# longest subarray with sum k
arr = list(map(int, input().split()))
k = int(input("enter sum: "))
summ  = 0
max_len = 0
i = 0
j = 0
while j < len(arr):
    summ += arr[j]
    if summ < k:
        j +=1
    elif summ == k:
        max_len = max(max_len , j-i+1)
        j+=1
    elif summ > k:
        while summ > k:
            summ -= arr[i]
            i+=1
        j+=1
print(max_len)
