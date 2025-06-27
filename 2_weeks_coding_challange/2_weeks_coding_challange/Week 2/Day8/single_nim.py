class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR cancels out pairs
        return result