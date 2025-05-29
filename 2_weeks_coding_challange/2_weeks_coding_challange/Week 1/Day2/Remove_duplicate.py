def removeDuplicates(nums):
        hashset = set()
        index = 0
        for i in nums:
            if i not in hashset:
                hashset.add(i)
                nums[index] = i
                index +=1
        print(index)
arr = [10,10,8,8,8,9,9,13,12]
removeDuplicates(arr)