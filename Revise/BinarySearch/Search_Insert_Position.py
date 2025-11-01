class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) -1
        index = len(nums)
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                index = mid
                end = mid -1
            else:
                start = mid + 1
        return index
