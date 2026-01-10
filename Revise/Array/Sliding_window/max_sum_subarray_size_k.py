# max sum subarray of size k 

nums = list(map(int, input().split()))
k = int(input("enter k: "))
# both start and end is initialized at beginning of array
i = 0
j = 0
summ = 0
max_sum = float('-inf')

while j < len(nums):
    summ += nums[j]
    if (j - i + 1) < k:
        j += 1
    elif (j - i + 1) == k:
        max_sum = max(max_sum, summ)
        summ -= nums[i]
        i += 1
        j += 1

print(max_sum)
