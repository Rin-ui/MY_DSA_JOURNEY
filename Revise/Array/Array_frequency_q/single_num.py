# single number

nums = list(map(int, input().split()))
dict = {}

for i in range(len(nums)):
    if nums[i] in dict:
        dict[nums[i]] += 1
    else:
        dict[nums[i]] = 1

for key in dict:
    if dict[key] == 1:
        print(key)
