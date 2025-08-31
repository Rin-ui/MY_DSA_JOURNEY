# print all elements in a 2d array 
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

# Row order
row = len(arr)
col = len(arr[0])
for i in range(row):
    for j in range(col):
        print(arr[i][j], end=" ")
    print()

print()
print()
# Column Order 
for j in range(col):
    for i in range(row):
        print(arr[i][j] , end=" ")
    print()
    
