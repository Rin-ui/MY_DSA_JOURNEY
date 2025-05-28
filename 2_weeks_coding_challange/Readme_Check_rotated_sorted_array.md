**Leetcode : WEEK 1 🡪 DAY 1**

**Question :**

[**Check if Array Is Sorted and Rotated**](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) **:**

**Question description:**

_Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false._

_There may be duplicates in the original array._

_Note: An array A rotated by x positions results in an array B of the same length such that B\[i\] == A\[(i+x) % A.length\] for every valid index i._

&nbsp;

_Example 1:_

_Input: nums = \[3,4,5,1,2\]_

_Output: true_

_Explanation: \[1,2,3,4,5\] is the original sorted array._

_You can rotate the array by x = 3 positions to begin on the element of value 3: \[3,4,5,1,2\]._

_Example 2:_

_Input: nums = \[2,1,3,4\]_

_Output: false_

_Explanation: There is no sorted array once rotated that can make nums._

_Example 3:_

_Input: nums = \[1,2,3\]_

_Output: true_

_Explanation: \[1,2,3\] is the original sorted array._

_You can rotate the array by x = 0 positions (i.e. no rotation) to make nums._

**_Answer:_**

1. _1<sup>st</sup> we need to understand is that the initially given array nums in question is not the original array ie ascending sorted array… rather the array given in question either could me rotated ascending array (rotation can be 0 also) or an array that is not ascendingly sorted_
2. **_My doubts:_**

- **_Do we have to write logic or conditions of rotation or sorted array? ( my mind was scattered as I was struggling to think of the sequence or way to solve)_**

**_Ans:_** _No_ _, we don’t need to write code of rotation or sorting…my mind was just stuck in limited thought I got by predone questions and unable to expand the logic… here the correct approach , here we just need to if the array is rotated ascending array or not , so we don’t have to separately write the either code but only a checking code._

- **_What is the logic for rotation of ascending array? Do we separately check condition? And in question we are given a modified array , how we will assume the original array how to think of approach?_**

**_Ans:_** _As we are told in the question to check if the array originally was ascendingly sorted , there for with respect to this we will check. Ascending means smaller to bigger value , there fore arr\[i\] &lt; arr\[i+1\].. and now if we are performing rotation a break inbetween array will take place ie violating the condition, at place where array is rotated the condition will be true for arr\[i\] &gt; arr\[i+1\] . Now as our main aim is to check for rotation in ascending array we can use this logic arr\[i\] > arr\[i+1\] with little modification at arr\[i+1\] as at last index ( lest last index = 4 , arr \[ I +1\] = 4+1= 5🡪index error) to avoid error we caqn add logic arr\[ (i+1) % len(arr)\] 🡪 this logic returns if last index greater than size of array it creates a circular fashion ie arr = \[1,2,3,4,5\] , len(arr) = 5 ,last index I = 4 (0 based index) arr\[(i+1)%len(arr)\] 🡪 arr\[4+1 % 5\] = arr\[5%5\] = arr\[0\] 🡪 hence index error avoided_

1. **_Code:_**

_def check(self, nums):_

&nbsp;       _n = len(nums)_

&nbsp;       _count = 0_

&nbsp;       _for i in range(len(nums)):_

&nbsp;           _if nums\[i\] > nums\[(i+1) % n\]:_

&nbsp;               _count +=1_

&nbsp;               _if count > 1:_

&nbsp;                   _return False_

&nbsp;       _return True_

1. **Count Logic** :

 ✅ If count == 0: It's **already sorted**.

 ✅ If count == 1: It's a **rotated** sorted array.

 ❌ If count > 1: It’s **not** a rotated sorted array.


