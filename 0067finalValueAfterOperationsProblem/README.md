# 📌 Final Value of Variable After Performing Operations

## 🔗 Problem Source

LeetCode: [https://leetcode.com/problems/final-value-of-variable-after-performing-operations/](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/)

---

## 🧩 Problem Description

A simple programming language contains only one variable `X` and four possible operations:

- `++X` or `X++` → increment `X` by 1
- `--X` or `X--` → decrement `X` by 1

The variable starts at `X = 0`.  
Given a list of operations, determine the final value of `X` after executing all of them sequentially.

---

## ✅ Examples

**Input:** `["--X","X++","X++"]`  
**Output:** `1`  

**Input:** `["++X","++X","X++"]`  
**Output:** `3`  

**Input:** `["X++","++X","--X","X--"]`  
**Output:** `0`

---

## 💡 Approach

1. Initialize a counter starting at zero.
2. Traverse the list of operations one by one.
3. Each operation either increases or decreases the counter by 1.
4. The position of `++` or `--` (prefix or postfix) does not matter—both have the same effect.

This leads to a straightforward linear scan solution without any complex parsing.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(n)`  
  Each operation is processed exactly once.

- **Space Complexity:** `O(1)`  
  Only a single integer variable is required.