# 📌 Suffix Sum Array Explanation  

For **suffix sum**, each `suffix[i]` stores the sum of elements from index `i` to the end of the array.  

---

### Example:
If  
\[
arr = [2, 4, 6, 8]
\]

Then,  

- `suffix[3] = arr[3] = 8`  
- `suffix[2] = suffix[3] + arr[2] = 8 + 6 = 14`  
- `suffix[1] = suffix[2] + arr[1] = 14 + 4 = 18`  
- `suffix[0] = suffix[1] + arr[0] = 18 + 2 = 20`  

So,  

\[
\text{suffix} = [20, 18, 14, 8]
\]

---

### 📌 Formula:
\[
suffix[i] = suffix[i+1] + arr[i]
\]

---

### ⚡ Important Detail:
- You should start **from the last index**.  
- The last element of suffix is just the last element of arr:  

\[
suffix[n-1] = arr[n-1] \quad \text{✅ correct}
\]
