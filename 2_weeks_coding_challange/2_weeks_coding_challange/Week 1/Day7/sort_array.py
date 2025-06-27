def insert_sorted(arr, value):
    # base case: if arr is empty or value is greater than last element
    if len(arr) == 0 or arr[-1] <= value:
        arr.append(value)
        return
    # remove the last element
    last = arr.pop()
    # recursive call to find correct position
    insert_sorted(arr, value)
    # put the removed element back
    arr.append(last)

def sorting_arr(arr):
    # base condition
    if len(arr) <= 1:
        return
    # remove last element
    last_ele = arr.pop()
    # sort the rest of the array
    sorting_arr(arr)
    # insert the last element into the sorted array
    insert_sorted(arr, last_ele)

    

