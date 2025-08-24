class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        maxi = -1
        # finding max
        for i in range(n):
            if arr[i] > maxi:
                maxi = arr[i]
        second = -1
        # finding second max or finding the element just before maximum
        for i in range(n):
            if arr[i] != maxi and arr[i] > second:
                second = arr[i]
        return second
