def max_diff(arr):
    min_val = arr[0]
    max_diff = float('-inf')
    for i in range(1, len(arr)):
        diff = arr[i] - min_val
        max_diff = max(max_diff, diff)
        min_val = min(min_val, arr[i])
    return max_diff
