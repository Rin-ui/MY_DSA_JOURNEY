def add(arr1,arr2):
    ans = []
    for i in range(len(arr1)):
        row = []   # create a new row
        for j in range(len(arr1[i])):
            row.append(arr1[i][j] + arr2[i][j])   # add element-wise
        ans.append(row)   # add row to ans
    
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()

arr1 = [
    [23,45,67,12],
    [11,22,33,44],
    [5,6,7,8]
]  

arr2 = [
    [34,54,77,90],
    [14,13,37,88],
    [66,29,58,31]
]

add(arr1,arr2)
