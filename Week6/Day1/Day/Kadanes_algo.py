def kadanes_algo(num):
    maxi = -1
    prefix = 0
    n = len(num)
    for i in range(n):
        prefix += num[i]
        maxi = max(maxi, prefix)
        if prefix < 0:
            prefix = 0
    return maxi
arr = [4,-6,2,8]
maxi = kadanes_algo(arr)
print(maxi)
