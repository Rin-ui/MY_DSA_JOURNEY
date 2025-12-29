#print table method 1
integer = int(input("enter an integer whose table you want to get: "))
for i in range(1,11):
    res = integer*i
    print(f"{integer} x {i} =",res)



#method 2 --> for a particular number
for i in range(1,11):
    print(6*i)

# method 3 ---> for a particular number
for i in range(6,61,6):
    print(i)
