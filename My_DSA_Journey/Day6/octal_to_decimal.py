octal = input("Enter an octal number: ")
octal = octal[::-1]
decimal = 0

for i in range(len(octal)):
    val = int(octal[i])         # convert character to integer
    decimal += val * (8 ** i)   # multiply by 8^i and add

print("Decimal equivalent:", decimal)

