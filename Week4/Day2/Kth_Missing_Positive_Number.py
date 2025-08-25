class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] - mid -1 >= k:
                end = mid -1
            else : 
                start = mid + 1
        return start + k
