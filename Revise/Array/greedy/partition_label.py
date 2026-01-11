# partition label 
string = list(input())
dict = {}

# from end iterate the string and put each char last position in hashmap
for i in range(len(string) - 1, -1, -1):
    if string[i] not in dict:
        # map element and its index
        dict[string[i]] = i
    else:
        continue

res = []
start = 0
end = 0

for i in range(len(string)):
    # extend partition till last occurrence of current character
    end = max(end, dict[string[i]])

    # if current index reaches partition end
    if i == end:
        res.append(end - start + 1)
        start = i + 1

print(res)
