class Solution:
    def minTime (self, arr, k):
        # code here
        ans = -1
        n = len(arr)
        start = max(arr)
        end = sum(arr)
        painter = 0
        work = 0
        if n==0 or k ==0 or n<k :
            return -1
        while start <= end:
            mid = (start + end)//2
            painter = 1
            work = 0
            for i in range(n):
                if work + arr[i] > mid:
                    painter +=1
                    work = arr[i]
                else:
                    work +=arr[i]
            if painter <= k:
                ans = mid
                end = mid -1
            else:
                start = mid + 1
        return ans
        
