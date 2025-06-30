def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    
    return prefix

def range_sum(prefix, li, ri):
    if li == 0:
        return prefix[ri]
    else:
        return prefix[ri] - prefix[li - 1]

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
prefix = build_prefix_sum(arr)

# Let's say we want to find sum from index 0 to 5
li = 0
ri = 5
ans = range_sum(prefix, li, ri)
print("Sum from index", li, "to", ri, "=", ans)
