# max average subarray of size k 

nums = list(map(int, input().split()))
k = int(input("enter k: "))
# both start and end is initialized at beginning of array
i = 0
j = 0
avg = 0
avg_cal = float('-inf')
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

avg_cal = max_sum / k
print(avg_cal)

   
