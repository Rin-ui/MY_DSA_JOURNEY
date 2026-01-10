# contains duplicate

nums = list(map(int, input().split()))
dict = {}

for i in range(len(nums)):
    if nums[i] in dict:
        print('True')
        break
    else:
        dict[nums[i]] = 1
