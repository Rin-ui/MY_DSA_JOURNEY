class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans = -1
        start = max(weights)
        end = sum(weights)
        w = 0
        d = 0
        n = len(weights)
        while start <= end:
            mid = (start + end)//2
            w = 0
            d =1
            if n == 0 or days == 0 or n < days:
                return -1
            for i in range(n):
                if w + weights[i] > mid:
                    d +=1
                    w = weights[i]
                else:
                    w +=weights[i]
            if d <=days:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
        
