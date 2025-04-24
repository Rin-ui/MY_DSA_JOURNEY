binary = input("Enter a binary number: ")
binary = binary[::-1]  # reverse the string
decimal = 0

for i in range(len(binary)):
    if binary[i] == '1':
        decimal += 2 ** i

print("Decimal equivalent:", decimal)
