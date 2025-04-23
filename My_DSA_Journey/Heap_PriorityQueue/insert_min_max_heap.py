def insert_max_heap(arr, val):
    arr.append(val)  # Increase heap size by appending the new value
    i = len(arr) - 1  # Index of newly inserted element
    
    # Restore the heap property by bubbling up
    while i > 0 and arr[(i-1)//2] < arr[i]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]  # Swap with parent
        i = (i-1)//2  # Move up to parent index


        
def insert_min_heap(arr, val):
    arr.append(val)  # Increase heap size by appending the new value
    i = len(arr) - 1  # Index of newly inserted element
    
    # Restore the heap property by bubbling up
    while i > 0 and arr[(i-1)//2] > arr[i]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]  # Swap with parent
        i = (i-1)//2  # Move up to parent index


