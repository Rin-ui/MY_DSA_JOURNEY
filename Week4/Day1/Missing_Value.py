class Solution:
    def missingNum(self, arr):
        # code here
        arr_sum = 0
        n = len(arr)
        total_sum = (n+1) * (n+2) // 2
        for i in range(n):
            arr_sum += arr[i]
        diff = total_sum - arr_sum
        return diff
