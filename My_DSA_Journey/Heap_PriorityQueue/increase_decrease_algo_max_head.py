def max_heapify(arr, i):
    largest = i  # Assume parent is the largest
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    n = len(arr)

    # Check if left child is greater
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child is greater
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap if needed and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Swapped {arr[i]} and {arr[largest]} in max_heapify")
        max_heapify(arr, largest)  # Recursive call

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):  # Start from last internal node
        max_heapify(arr, i)

def increase_key_max_heap(arr, i, new_ele):
    # Replacing an element in max heap with a higher value
    if arr[i] > new_ele:
        print('Wrong operation')
        return
    else:
        arr[i] = new_ele  # Assign the new value

    # Bubble up the element to maintain max heap property
    while i > 0 and arr[(i - 1) // 2] < arr[i]:  # Correct parent condition
        arr[(i - 1) // 2], arr[i] = arr[i], arr[(i - 1) // 2]  # Swap
        i = (i - 1) // 2  # Move to the parent index

def decrease_key_max_heap(arr,i,new_element):
    if new_element > arr[i]:
        print('wrong operation')
        return # so that loop stops
    else:
        arr[i]= new_element
        max_heapify(arr,i)


# Example usage:
arr = [34, 56, 3, 76, 8, 91, 90, 43, 24, 33]

print("\nBuilding Max Heap:")
build_max_heap(arr)
print("Max Heap:", arr)
increase_key_max_heap(arr,4,100)
print('increase an element in max heap', arr)
decrease_key_max_heap(arr,6,12)
print("decrease an element in max heap",arr)
