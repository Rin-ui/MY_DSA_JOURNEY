# min number of coins
N = int(input("enter a number: "))
choice = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
d = 0
result_list = [] # Renamed 'list' to 'result_list' to avoid shadowing the built-in type

while N > 0:
    for c in range(len(choice)):
        if N // choice[c] == 0:
            continue
        else:
            # First, find out how many times the coin fits
            d = N // choice[c]
            
            # Add that many coins to your list
            for count in range(d):
                result_list.append(choice[c])
            
            # NOW update N to the remainder
            N = N % choice[c]
                
print(result_list)
