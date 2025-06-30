def longestSubarray(self, nums, k):
        start = 0
        end = 0
        maxi = 0
        summ = 0
        while end < len(nums):
            summ = summ + nums[end]
            if summ < k:
                end += 1
            elif summ == k:
                maxi = max(maxi, end - start + 1)
                end += 1
            else:
                while summ > k and start < end:
                    summ = summ - nums[start]
                    start += 1
                end += 1
        return maxi
