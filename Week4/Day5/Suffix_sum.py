def suffix_sum(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]
    return suffix
