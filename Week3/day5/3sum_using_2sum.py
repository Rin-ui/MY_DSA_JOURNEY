def threeSum(nums, x):
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        target = x - nums[i]
        start = i + 1
        end = n - 1

        while start < end:
            if nums[start] + nums[end] == target:
                return [nums[i], nums[start], nums[end]]
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1

    return []
