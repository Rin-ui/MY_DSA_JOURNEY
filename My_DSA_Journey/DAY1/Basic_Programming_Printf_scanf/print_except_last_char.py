string = input("Enter a string: ")

for i in range(len(string) - 1):  # loop from i = 0 to i = len(string) - 2
    if string[i + 1] == " ":
        continue
    else:
        print(string[i], end =" ")
