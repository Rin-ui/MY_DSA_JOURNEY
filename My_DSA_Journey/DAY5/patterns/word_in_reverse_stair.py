string = input("Enter a string: ") 
words = string.split()

# We'll start indenting from the rightmost word
# For 3 words, indents = [4, 2, 0]
spaces = 2 * (len(words) - 1)

for word in words:
    print(" " * spaces + word)
    spaces -= 2
