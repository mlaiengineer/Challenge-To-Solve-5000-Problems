# 🗓️ Today’s Progress — 2025-12-02

Today I solved a digit-analysis problem where the goal is to count how many digits of an integer **evenly divide the number itself**.  
Digits are checked one by one, and digit `0` must be ignored since division by zero is undefined.

---
## 🔗 Problem Source  
GeeksForGeeks Problem: **Count Digits**  
https://www.geeksforgeeks.org/problems/count-digits5716/1?page=2&sortBy=submissions
## 🚀 Problem Summary

Given a positive integer `n`:

- Convert the number into individual digits.
- Count how many of those digits divide `n` with no remainder.
- Ignore digits that are `0`.

### Example
Input: 12 → Output: 2

Digits 1 and 2 both divide 12 evenly.


---

## 🧠 Approach

To solve this:

1. Convert the number to a string to easily iterate through its digits.
2. For each digit:
   - Skip if it is `0`.
   - Convert it back to an integer and check if `n % digit == 0`.
3. Increment a counter whenever a digit divides the number evenly.

This approach is clean, simple, and efficient.

---

## ⏱️ Complexity Analysis

### **Time Complexity: O(d)**  
Where `d` is the number of digits in `n`.  
We process each digit exactly once.

### **Space Complexity: O(1)**  
Only a few variables are used; no additional data structures.

---

## 🧩 Final Code

```python
class Solution:
    def evenlyDivides(self, n):
        num_str = str(n)
        count = 0

        for digit in num_str:
            d = int(digit)
            if d == 0:
                continue
            if n % d == 0:
                count += 1

        return count
