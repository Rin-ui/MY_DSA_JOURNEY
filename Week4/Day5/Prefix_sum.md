# 📌 Prefix Sum Array Explanation  

The correct formula for a prefix sum array is:  

$$
prefix[i] = prefix[i-1] + arr[i]
$$


---

### ✅ Explanation:
- `prefix[i]` means the sum of elements from index `0` to `i`.  
- To compute it, you take the sum up to `i-1` (`prefix[i-1]`) and add the current element `arr[i]`.

---

### Example:
If  
\[
arr = [2, 4, 6, 8]
\]

Then,  

- `prefix[0] = arr[0] = 2`  
- `prefix[1] = prefix[0] + arr[1] = 2 + 4 = 6`  
- `prefix[2] = prefix[1] + arr[2] = 6 + 6 = 12`  
- `prefix[3] = prefix[2] + arr[3] = 12 + 8 = 20`  

So,  

\[
\text{prefix} = [2, 6, 12, 20]
\]

---

### 📌 Small Detail:
- In **mathematical notation**, people often use parentheses: `prefix(i)`  
- In **programming**, we almost always use array notation: `prefix[i]`.
