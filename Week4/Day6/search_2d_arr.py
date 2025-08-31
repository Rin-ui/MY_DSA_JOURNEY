def search(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return (i, j)
    return None

   
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
search(arr,5)
