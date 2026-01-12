# power of a number
base = int(input("enter base: "))
exp = int(input("enter power: "))
nums = base
for i in range(1,exp):
    nums = nums * base
print(nums)
