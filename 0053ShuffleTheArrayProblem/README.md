# 🗓️ Today’s Progress — 2025-11-30  

Today (2025-11-30) I solved the LeetCode problem **“Shuffle the Array.”**  
The problem requires rearranging an array of length `2n` from the format:

[x1, x2, ..., xn, y1, y2, ..., yn]


into:

[x1, y1, x2, y2, ..., xn, yn]


---

## 🚀 Approach  

To solve this problem, I used a **splitting + slice assignment** technique:

1. **Split** the array into two halves:  
   - First half → `x = nums[:n]`  
   - Second half → `y = nums[n:]`

2. **Prepare a result array** of size `2n`.

3. **Use slice assignment with steps** to interleave values:  
   - Even indices (`0, 2, 4...`) → filled with `x`  
   - Odd indices (`1, 3, 5...`) → filled with `y`

This method is clean, Pythonic, and efficient.

---

## ⏱️ Complexity Analysis  

### **Time Complexity: O(n)**  
Because:
- Splitting the array takes O(n)  
- Assigning elements using slice stepping also takes O(n)  
No nested loops are used.

### **Space Complexity: O(n)**  
Because:
- Two new lists (`x` and `y`) of size `n` are created  
- A final list of size `2n` is created  
The extra memory used grows proportionally with the input size.

---

## 🔗 Problem Source  
LeetCode Problem: **Shuffle the Array**  
https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
