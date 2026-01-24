## 📌 Palindrome Partitioning

### 🔗 Problem Source
LeetCode: https://leetcode.com/problems/palindrome-partitioning/

---

## 🧩 Problem Summary

Given a string `s`, partition it into substrings such that **every substring is a palindrome**.  
Return **all possible palindrome partitions** of the string.

A palindrome is a string that reads the same forward and backward.

---

## 💡 Solution Approach (Summary)

The solution combines **Dynamic Programming** and **Backtracking**:

1. **Preprocessing with Dynamic Programming**  
   A 2D table is used to determine whether any substring `s[i..j]` is a palindrome.  
   This allows constant-time palindrome checks during partitioning.

2. **Backtracking to Generate Partitions**  
   Starting from the first character, the algorithm recursively builds partitions by choosing
   valid palindromic substrings and exploring all possible combinations.

This approach efficiently avoids repeated palindrome checks and ensures all valid partitions are found.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(n · 2^n)`  
  Each character can either start a new partition or extend an existing one.

- **Space Complexity:** `O(n²)`  
  Used by the palindrome DP table and recursion stack.

---

## 🎯 Key Takeaways

- Demonstrates effective use of **DP + Backtracking**
- Shows understanding of **optimization through preprocessing**
- Clean separation between validation (palindrome checking) and generation (partitioning)
- Scales efficiently within given constraints

---


