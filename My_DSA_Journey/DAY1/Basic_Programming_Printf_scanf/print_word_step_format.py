string = input("enter a string: ")
words = string.split()
position =0
for word in words:
    print(" "*position + word)
    position += len(word)

