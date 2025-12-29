# check power of a number
n = int(input("enter an base in integer: "))
power = int(input("enter an power integer: "))
nums = n
for i in range(1, power):
    nums = nums * n
print(nums)
