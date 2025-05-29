**_Question :_**  [**_Remove Duplicates from Sorted Array_**](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given an integer array nums sorted in **non-decreasing order**, remove the duplicates [**in place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return _the number of unique elements in_ nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Custom Judge:**

The judge will test your solution with the following code:

int\[\] nums = \[...\]; // Input array

int\[\] expectedNums = \[...\]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;

for (int i = 0; i < k; i++) {

assert nums\[i\] == expectedNums\[i\];

}

If all assertions pass, then your solution will be **accepted**.

&nbsp;

**Example 1:**

**Input:** nums = \[1,1,2\]

**Output:** 2, nums = \[1,2,\_\]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

**Input:** nums = \[0,0,1,1,1,2,2,3,3,4\]

**Output:** 5, nums = \[0,1,2,3,4,\_,_,\_,_,\_\]

**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).

**_Answer:_**

1. _Few misunderstandings to avoid as I encountered them while doing 🡪 We don’t have to print the underscores. The_ **_underscores in the example are just placeholders_**_. They are used_ **_for illustration purposes only_** _— to show that the values_ **_after the first k elements do not matter_**_._

**_The underscores are not something you actually put into the array._**

**_Here's what the problem really wants:_**

_Modify the nums array_ **_in-place_**_._

_Ensure that the_ **_first k elements_** _of nums contain the unique values in order._

_Return the value k (i.e. the number of unique elements)._

**_Ignore everything after k — they can be any value._**

1. **_Code_**

_class Solution(object):_

_def removeDuplicates(self, nums):_

_hashset = set()_

_index = 0 # Pointer to place unique elements_

_for i in nums:_

_if i not in hashset:_

_hashset.add(i)_

_nums\[index\] = i_

_index += 1_

_return index # This is the count of unique elements_

1. _Explaination:_

**def removeDuplicates(self, nums):**

- _This defines the_ **_method_** _called removeDuplicates inside the Solution class._
- _It takes:_
  - _self → a reference to the object (required in class methods)._
  - _nums → the input list of integers,_ **_sorted in non-decreasing order_**_._

**_hashset = set()_**

- _Creates an_ **_empty set_** _called hashset._
- _Sets automatically_ **_ignore duplicates_**_, which makes them perfect for tracking_ **_unique values_**_._
- _Purpose: To_ **_store unique elements_** _we’ve already seen while looping through nums._

**_index = 0_**

- _This is a pointer that_ **_marks the position in nums_** _where the next unique value should be written._
- _Purpose: Helps modify the array_ **_in-place_**_._

**_for i in nums:_**

- _Loop through each element i in the input list nums._

**_if i not in hashset:_**

- _Check whether the value i has already been added to hashset:_
  - _If it's already there, skip it (it's a duplicate)._
  - _If it’s_ **_not_** _there, it means i is a_ **_new unique element_**_._

**_hashset.add(i)_**

- _Add this new unique value i to the set, so we remember we’ve seen it._
- _This helps prevent adding the same value again later._

**_nums\[index\] = i_**

- _Write the current unique value i to the index-th position in the original nums list._
- _Purpose: Overwrite nums in-place so the_ **_first k elements are unique values_**_._

**_index += 1_**

- _Move the index forward by 1, so the next unique element goes into the next position._

**_return index_**

- _At the end, return index, which now represents:_
  - _The total number of_ **_unique elements_**_._
  - _The length k such that nums\[:k\] contains all the unique values._

1. **Example**

Input: nums = \[1, 1, 2, 3, 3\]

| **Step** | **i** | **hashset** | **nums after writing** | **index** |
| --- | --- | --- | --- | --- |
| 1   | 1   | {1} | \[1, 1, 2, 3, 3\] | 1   |
| 2   | 1   | already in set | skip | 1   |
| 3   | 2   | {1, 2} | \[1, 2, 2, 3, 3\] | 2   |
| 4   | 3   | {1, 2, 3} | \[1, 2, 3, 3, 3\] | 3   |
| 5   | 3   | already in set | skip | 3   |

Return value: 3
