# longest substring with no repeating characters
arr = list(input().split())
k = int(input("enter no of unique characters: "))
dict = {}
i = 0
j = 0
max_len = 0

while j < len(arr):
    # no of occ of each character we'll get from val of hashmap
    if arr[j] not in dict:
        dict[arr[j]] = 1
    else:
        dict[arr[j]] += 1

    if dict[arr[j]] == 1:
        max_len = max(max_len, j - i + 1)
        j += 1

    elif dict[arr[j]] > 1:
        # removing calculation of i
        while dict[arr[j]] > 1:
            dict[arr[i]] -= 1
            if dict[arr[i]] == 0:
                del(dict[arr[i]])
            i += 1
        j += 1

print(max_len)
