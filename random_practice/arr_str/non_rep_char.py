s = input()
store = {}
for i in s:
    if i not in store:
        store[i] = 1
    else:
        store[i] +=1
for key , val in store.items():
    if store[key] ==1:
        print(key)
        break
