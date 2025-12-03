# 🗓️ Today’s Progress — 2025-12-03

Today I solved the LeetCode problem **“Palindrome Number.”**  
The task is to determine whether a given integer reads the same forward and backward.

---

## 🧠 Problem Summary

A number is a **palindrome** if it remains identical when reversed.

### Examples
Input: 121 → Output: true

Input: -121 → Output: false

Input: 10 → Output: false


A negative number is never a palindrome because of the leading `-` sign.

---

## 🚀 Approach

For this solution, I used a **string-based approach**:

1. Convert the integer `x` into a string.
2. Reverse the string manually using a loop.
3. Compare the original and reversed strings.
4. If they match → return `True`.

This method is simple and easy to understand.

---

## ⏱️ Complexity Analysis

### **Time Complexity: O(n)**  
Where `n` is the number of digits.  
We iterate once to build the reversed string.

### **Space Complexity: O(n)**  
We store the reversed string separately.

---

## 🔗 Problem Source  
https://leetcode.com/problems/palindrome-number/

---

## 🧩 Final Code

```python
class Solution(object):
    def isPalindrome(self, x):
        convert_x_to_str = str(x)
        reverse_x = ""
        for digit in convert_x_to_str:
            reverse_x = digit + reverse_x
        return convert_x_to_str == reverse_x
