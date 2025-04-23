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

# EXTRACT 

def extract_max_in_max_heap(arr):
    if len(arr) < 1:
        print('Heap underflow')
        return None  # Return None to indicate failure

    max_value = arr[0]  # Store max (root)
    
    arr[0], arr[-1] = arr[-1], arr[0]  # Swap root with last element
    arr.pop()  # Remove last element (which was the max)
    
    if len(arr) > 0:  # Only heapify if elements remain
        max_heapify(arr, 0)

    return max_value  # Return the extracted max

def extract_min_in_min_heap(arr):
    if len(arr) < 1:
        print('Heap underflow')
        return None  # Return None to indicate failure

    min_value = arr[0]  # Store min (root)
    
    arr[0], arr[-1] = arr[-1], arr[0]  # Swap root with last element
    arr.pop()  # Remove last element (which was the min)
    
    if len(arr) > 0:  # Only heapify if elements remain
        min_heapify(arr, 0)

    return min_value  # Return the extracted min

