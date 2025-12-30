# fibonacci
last = 0
prev = 1
curr = 0

n = int(input("enter a number till which you want the series: "))

print(last)
print(prev)

for i in range(n - 2):
    curr = prev + last
    print(curr)
    last = prev
    prev = curr
