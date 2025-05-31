def rotate(nums, k):
        k = k % len(nums)
        if k ==0 :
            return nums
        nums[:] = nums[-k : ] + nums[ : -k]