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


def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        print(f"Swapped {arr[0]} and {arr[i]} in heap_sort")
        max_heapify(arr, 0)  # Restore heap property


