def check(nums):
        n = len(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % n]:
                count +=1
                if count > 1:
                    print(False)
        print(True)

n = [3,4,5,1,2]
check(n)