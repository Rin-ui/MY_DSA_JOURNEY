class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                find = target - nums[i] - nums[j]
                start = j + 1
                end = n - 1
                self.twosum(nums, find, i, j, start, end, res)

        return list(res)

    def twosum(self, nums, find, i, j, start, end, res):
        while start < end:
            two_sum = nums[start] + nums[end]
            if two_sum == find:
                quad = (nums[i], nums[j], nums[start], nums[end])
                res.add(quad)
                start += 1
                end -= 1
            elif two_sum < find:
                start += 1
            else:
                end -= 1
