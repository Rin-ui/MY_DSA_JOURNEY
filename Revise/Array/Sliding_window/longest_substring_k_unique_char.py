# longest substring with k unique characters
arr = list(input().split())
k = int(input("enter no of unique characters: "))
dict = {}
i = 0
j = 0
max_len = 0

while j < len(arr):
    # no of unique character we'll get from size of hashmap
    if arr[j] not in dict:
        dict[arr[j]] = 1
    else:
        dict[arr[j]] += 1

    if len(dict) < k:
        j += 1

    elif len(dict) == k:
        max_len = max(max_len, j - i + 1)
        j += 1

    elif len(dict) > k:
        # removing calculation of i
        while len(dict) > k:
            dict[arr[i]] -= 1
            if dict[arr[i]] == 0:
                del(dict[arr[i]])
            i += 1
        j += 1

print(max_len)
