# majority element optimal

nums = list(map(int, input().split()))
dict = {}

for i in range(len(nums)):
    if nums[i] in dict:
        dict[nums[i]] += 1
    else:
        dict[nums[i]] = 1

print(max(dict, key=dict.get))
