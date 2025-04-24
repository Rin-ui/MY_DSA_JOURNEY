decimal = int(input("enter decimal number: "))
n = decimal
hexadecimal = " "
while n!=0:
    rem = n % 16
    hexadecimal = str(rem) + hexadecimal
    n = n // 16

print(hexadecimal)
