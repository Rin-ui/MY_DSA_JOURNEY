def Fibonacci(arr, pos):
    arr[0] = 0
    arr[1] = 1
    for i in range(2, pos):
        arr[i] = arr[i-1] + arr[i-2]
    return arr, arr[pos-1]   # return sequence and nth number

# Example
n = 7
arr = [0] * n
seq, last = Fibonacci(arr, n)
print("Sequence:", seq)
print("7th Fibonacci:", last)
