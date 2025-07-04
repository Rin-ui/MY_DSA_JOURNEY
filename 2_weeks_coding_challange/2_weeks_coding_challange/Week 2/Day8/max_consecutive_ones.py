class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count +=1
                max_count = max(current_count, max_count)
            else:
                current_count = 0
        return max_count