# print nth fibinacci number 

last = 0
prev = 1
curr = 0

n = int(input("enter a number which fib num we want: "))

for i in range(n - 2):
    curr = prev + last
    last = prev
    prev = curr

print(curr)
