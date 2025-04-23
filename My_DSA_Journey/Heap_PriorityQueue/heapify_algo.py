def max_heapify(arr, i):
    largest = i  # Assume parent is the largest
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    n = len(arr)
    
    print(f"{arr} before max_heapify")
    
    # Check if left child is greater
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child is greater
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap if needed and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Swapped {arr[i]} and {arr[largest]}")
        max_heapify(arr, largest)  # Recursive call

    print(f"{arr} after max_heapify")


def min_heapify(arr, i):
    smallest = i  # Assume parent is the smallest
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    n = len(arr)
    
    print(f"{arr} before min_heapify")
    
    # Check if left child is smaller
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    # Check if right child is smaller
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    # Swap if needed and heapify the affected subtree
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        print(f"Swapped {arr[i]} and {arr[smallest]}")
        min_heapify(arr, smallest)  # Corrected recursive call

    print(f"{arr} after min_heapify")


# Example usage:
arr = [34, 56, 3, 76, 8, 91, 90, 43, 24, 33]

print("\nApplying Max Heapify:")
max_heapify(arr, 0)  # Fixing only the root node

print("\nApplying Min Heapify:")
min_heapify(arr, 0)  # Fixing only the root node


