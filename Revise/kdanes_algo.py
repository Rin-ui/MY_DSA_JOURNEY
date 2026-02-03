class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        prefix = 0
        n = len(nums)
        for i in range(n):
            prefix = prefix +nums[i]
            maxi = max(maxi,prefix)
            if prefix < 0:
                prefix = 0
        return maxi
