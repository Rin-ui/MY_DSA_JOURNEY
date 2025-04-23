string = input("enter a string: ")
length = len(string)
for i in range(len(list(string))):
    print(" "* (length -i-1) + string[i])
    