hexadecimal = input("Enter a hexadecimal number: ")
hexadecimal = hexadecimal[::-1]
decimal = 0

for i in range(len(hexadecimal)):
    ch = hexadecimal[i].upper()  # in case user enters lowercase
    if ch.isdigit():
        val = int(ch)
    else:
        val = ord(ch) - ord('A') + 10  # convert 'A'-'F' to 10-15

    decimal += val * (16 ** i)

print("Decimal equivalent:", decimal)
