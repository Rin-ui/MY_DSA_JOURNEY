# pivot index
nums = list(map(int, input().split()))
i = 0
j = len(nums) - 1

def prefix_sum(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]
    return prefix

def suffix_sum(nums):
    suffix = [0] * len(nums)
    suffix[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i]
    return suffix

prefix = prefix_sum(nums)
suffix = suffix_sum(nums)

while i < len(nums):
    left_sum = prefix[i - 1] if i > 0 else 0
    right_sum = suffix[i + 1] if i < len(nums) - 1 else 0

    if left_sum == right_sum:
        print(f"pivot index is {i}")
        break
    i += 1
else:
    print("pivot index not found")
