class Solution:
    def search(self, arr, x):
        # code here
        n = len(arr)
        for i in range(n):
            if arr[i] == x:
                index = i
                break
        else:
            return -1
        return index
