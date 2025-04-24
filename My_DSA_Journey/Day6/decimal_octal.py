decimal = int(input("enter decimal number: "))
n = decimal
octal = " "
while n!=0:
    rem = n % 8
    octal = str(rem) + octal
    n = n // 8

print(octal)
