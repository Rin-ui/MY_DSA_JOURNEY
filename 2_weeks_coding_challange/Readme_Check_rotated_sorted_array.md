Leetcode : WEEK 1  DAY 1 
Question :
Check if Array Is Sorted and Rotated : 
Question description: 
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
 
Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

Answer: 
1.	1st we need to understand is that the initially given array nums in question is not the original array ie ascending sorted array… rather the array given in question either could me rotated ascending array (rotation can be 0 also)  or an array that is not ascendingly sorted
2.	My doubts:  
•	Do we have to write logic or  conditions of rotation or sorted array? ( my mind was scattered as I was struggling to think of the sequence or way to solve)

Ans: No , we don’t need to write code of rotation or sorting…my mind was just stuck in limited thought I got by predone questions and unable to expand the logic… here the correct approach , here we just need to if the array is rotated ascending array or not , so we don’t have to separately write the either code but only a checking code.

•	What is the logic for rotation of ascending array? Do we separately check condition? And in question we are given a modified array , how we will assume the original array how to think of approach?

Ans: As we are told in the question to check if the array originally was ascendingly sorted , there for with respect to this we will check. Ascending means smaller to bigger value  , there fore arr[i] < arr[i+1].. and now if we are performing rotation a break inbetween array will take place ie violating the condition, at place where array is rotated the condition will be true for arr[i] > arr[i+1] . Now as our main aim is to check for rotation in ascending array we can use this logic arr[i] > arr[i+1] with little modification at arr[i+1] as at last index ( lest last index  = 4  , arr [ I +1] = 4+1= 5index error) to avoid error we caqn add logic arr[ (i+1) % len(arr)]  this logic returns if last index greater than size of array it creates a circular fashion ie arr = [1,2,3,4,5] , len(arr) = 5 ,last index I = 4 (0 based index) arr[(i+1)%len(arr)]  arr[4+1 % 5] = arr[5%5] = arr[0]   hence index error avoided
3.	Code:
def check(self, nums):
        n = len(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % n]:
                count +=1
                if count > 1:
                    return False
        return True
4.	Count Logic :
•  ✅ If count == 0: It's already sorted.
•  ✅ If count == 1: It's a rotated sorted array.
•  ❌ If count > 1: It’s not a rotated sorted array.



