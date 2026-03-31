s=input()
countS = {}
arr=[]
for i in s:
    if i not in countS:
        countS[i]=1
    else:
        countS[i]+=1
for key,val in countS.items():
    print(f"{key}{val}", end = "")

