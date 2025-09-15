def add_ele(n):
    # Base condition
    if n == 0:
        return 0
    # Hypothesis + Induction
    return (n % 10) + add_ele(n // 10)

# Example
n = 1234
print("Sum of digits:", add_ele(n))  # Output: 10
