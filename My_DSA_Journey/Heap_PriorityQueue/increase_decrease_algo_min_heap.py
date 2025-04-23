def min_heapify(arr, i):
    smallest = i  # Assume parent is the smallest
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    n = len(arr)

    # Check if left child is smaller
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    # Check if right child is smaller
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    # Swap if needed and heapify the affected subtree
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        print(f"Swapped {arr[i]} and {arr[smallest]} in min_heapify")
        min_heapify(arr, smallest)  # Corrected recursive call
    
def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):  # Start from last internal node
        min_heapify(arr, i)

def decrease_key_min_heap(arr, i, new_element):
    if new_element > arr[i]:
        print('Wrong operation: New element is larger than the current element')
        return
    else:
        arr[i] = new_element

        # Bubble up to restore heap property
        while i > 0 and arr[(i-1)//2] > arr[i]:
            arr[(i-1)//2], arr[i] = arr[i], arr[(i-1)//2]
            i = (i-1)//2  # Update the index to the parent's index for the next comparison
def increase_key_min_heap(arr,i,new_element):
    if new_element < arr[i]:
        print('Wrong operation: New element is larger than the current element')
        return
    else:
        arr[i] = new_element
        min_heapify(arr,i)