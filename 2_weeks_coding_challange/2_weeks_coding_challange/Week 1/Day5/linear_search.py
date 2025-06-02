def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"{target} found at index {i}")
            return
    print("Not found")

arr = [4, 8, 9, 7, 5, 12]
t = 7
linear(arr, t)
