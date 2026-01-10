# First -ve in every window of size k

arr = list(map(int, input().split()))
k = int(input("enter k: "))
# both start and end is initialized at beginning of array
i = 0
j = 0
queue = []

neg = []   # to store negative numbers in current window

while j < len(arr):
    if arr[j] < 0:
        neg.append(arr[j])

    if (j - i + 1) < k:
        j += 1
    elif (j - i + 1) == k:
        if len(neg) > 0:
            queue.append(neg[0])
        else:
            queue.append(0)

        if arr[i] < 0:
            neg.pop(0)

        i += 1
        j += 1

print(queue)
