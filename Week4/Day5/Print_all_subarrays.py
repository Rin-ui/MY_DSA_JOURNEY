def print_all_subarrays(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            print(arr[i:j+1])
