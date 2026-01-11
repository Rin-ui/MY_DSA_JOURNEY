# min no of coin
options = list(map(int, input().split()))  # coin denominations
n = int(input("enter amount: "))           # total amount
temp = n
count = 0

options.sort(reverse=True)  # greedy needs largest first

while n > 0:
    for coin in options:
        if n >= coin:
            use = n // coin
            count += use
            n = n % coin

print("minimum number of coins:", count)
