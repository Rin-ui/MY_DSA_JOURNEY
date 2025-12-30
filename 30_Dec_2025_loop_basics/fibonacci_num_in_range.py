# fibonacci numbers in a given range
start = int(input("enter starting range: "))
end = int(input("enter ending range: "))

last = 0
prev = 1

while last <= end:
    if last >= start:
        print(last)
    curr = last + prev
    last = prev
    prev = curr
