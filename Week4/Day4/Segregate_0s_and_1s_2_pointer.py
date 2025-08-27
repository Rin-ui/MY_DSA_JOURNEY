# 2 pointer approach 
class Solution:
    def segregate0and1(self, arr):
        # code here
        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] ==0:
                start +=1
            else:
                if arr[end] ==0:
                    arr[start],arr[end] = arr[end],arr[start]
                    start+=1
                    end-=1
                else:
                    end-=1
