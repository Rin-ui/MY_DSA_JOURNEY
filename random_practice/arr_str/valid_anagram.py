s=input()
t=input()
countS = {}
countT = {}
for i in s:
    if i not in countS:
        countS[i] = 1
    else:
        countS[i] +=1
for i in t:
    if i not in countT:
        countT[i] = 1
    else:
        countT[i] +=1
if countS == countT:
    print("anagram")
else:
    print("not anagram")
