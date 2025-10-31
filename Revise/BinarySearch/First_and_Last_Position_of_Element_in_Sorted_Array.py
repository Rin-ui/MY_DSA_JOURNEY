class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # we'll work with 2 loops , one to find 1st occ and one to find 2nd occ
        start = 0
        end = len(nums) - 1
        first = -1
        last = -1

        # finding 1st occ --> here we'll 1st find target then check left half
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        # if target not found at all, return early
        if first == -1:
            return [ -1, -1 ]

        # reset search boundaries for finding last occurrence
        start = 0
        end = len(nums) - 1

        # finding last occurance --> find target and check right half
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                last = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [first, last]
