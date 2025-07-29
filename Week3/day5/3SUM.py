class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n - 2):
            # To avoid duplicates at the start
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 1):
                # To avoid duplicates in second pointer
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                target = 0 - nums[i] - nums[j]
                # Binary search the third element from j+1 to end
                if self.binary_search(nums, j + 1, n - 1, target):
                    res.add((nums[i], nums[j], target))

        return [list(triplet) for triplet in res]

    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
