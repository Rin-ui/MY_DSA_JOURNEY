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


def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):  # Start from last internal node
        max_heapify(arr, i)


def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):  # Start from last internal node
        min_heapify(arr, i)


# Example usage:
arr = [34, 56, 3, 76, 8, 91, 90, 43, 24, 33]

print("\nBuilding Max Heap:")
build_max_heap(arr)
print("Max Heap:", arr)

arr = [34, 56, 3, 76, 8, 91, 90, 43, 24, 33]  # Reset array

print("\nBuilding Min Heap:")
build_min_heap(arr)
print("Min Heap:", arr)
