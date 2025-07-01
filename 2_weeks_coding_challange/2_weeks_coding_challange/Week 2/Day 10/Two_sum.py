class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[n] = i
                