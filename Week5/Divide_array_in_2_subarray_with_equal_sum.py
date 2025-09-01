def two_subarray_equal_sum(arr):
    total_sum = sum(arr)
    prefix_sum = 0
    n = len(arr)
    ans = -1
    for i in range(n-1):  # stop at n-2, so right subarray is not empty
        prefix_sum += arr[i]
        ans = total_sum - prefix_sum
        if ans == prefix_sum:
            subarray1 = arr[0:i+1]
            subarray2 = arr[i+1:n]
            print("Subarray 1:", subarray1)
            print("Subarray 2:", subarray2)
            return True
    return False

arr = [3,4,-2,5,8,20,-10,8]
print(two_subarray_equal_sum(arr))
