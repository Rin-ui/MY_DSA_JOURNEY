string = input("Enter string: ")
words = string.split()
n = len(words)

for i in range(n):
    ch = words[i][0].upper()  # get the first letter and capitalize it
    print(" " * (n - i - 1) + (ch + " ") * (i + 1))


