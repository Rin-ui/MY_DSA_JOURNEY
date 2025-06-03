**Missing Values:** 

**🔍 Problem Recap:**

You are given an array nums with **n distinct numbers**, all from the range [0, n]. That means you're given numbers from 0 up to n, but **one number is missing**.

Your task is to **find that missing number**.

-----
**✅ Let's Understand With an Example:**

Let’s take this:

nums = [3, 0, 1]

- There are 3 elements, so n = 3
- The range should be [0, 1, 2, 3]
- But the array only has [3, 0, 1] → so what’s missing? **2**
-----
**🧠 Intuition and Trick:**

All numbers from 0 to n are expected.

So if you calculate the **sum of all numbers from 0 to n**, and subtract the **sum of the numbers in the array**, you’ll get the **missing number**.

This works because:

(0 + 1 + 2 + ... + n) - (sum of nums) = missing number

-----
**📐 Formula:**

The sum of first n natural numbers is:

total = n \* (n + 1) // 2

**✏️ Code:**

def missingNumber(nums):

`    `n = len(nums)

`    `total = n \* (n + 1) // 2

`    `return total - sum(nums)

-----
**🔍 Let’s Apply On Example 3:**

pgsql

CopyEdit

nums = [9,6,4,2,3,5,7,0,1]

n = 9 (since there are 9 numbers → so expected range is 0 to 9)

Total sum from 0 to 9 = 9 \* (9 + 1) / 2 = 45

Sum of nums = 9+6+4+2+3+5+7+0+1 = 37

Missing = 45 - 37 = 8 ✅

-----
**🧪 Test the Function:**

print(missingNumber([3,0,1]))       # Output: 2

print(missingNumber([0,1]))         # Output: 2

print(missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8

