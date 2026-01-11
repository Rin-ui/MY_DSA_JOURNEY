# running sum
nums = list(map(int, input().split()))
prefix = [0] * len(nums)
prefix[0] = nums[0]
for i in range(len(nums)):
    prefix[i] = prefix[i-1] + nums[i]
print(prefix)
