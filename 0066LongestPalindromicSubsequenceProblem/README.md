# Longest Palindromic Subsequence

## 🔗 Problem Source
LeetCode: https://leetcode.com/problems/longest-palindromic-subsequence/

---

## 📌 Problem Description

Given a string **s**, find the length of the **longest palindromic subsequence** in `s`.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements **without changing the order** of the remaining elements.

---

## ✅ Examples

### Example 1
Input:
s = "bbbab"

Output:
4

Explanation: One possible longest palindromic subsequence is `"bbbb"`.

### Example 2
Input:
s = "cbbd"

Output:
2

Explanation: One possible longest palindromic subsequence is `"bb"`.

---

## 🧠 Approach

This solution uses **Dynamic Programming**.

### Idea

Let:

dp[i][j] = length of the longest palindromic subsequence in substring s[i..j]


We build the table diagonally:

- If `i == j` → single character → palindrome of length 1  
- If `s[i] == s[j]` →  dp[i][j] = 2 + dp[i+1][j-1]
- Else → dp[i][j] = max(dp[i+1][j], dp[i][j-1])


Final answer will be stored in: dp[0][n-1]

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(n²)`  
  - We fill an `n x n` DP table.

- **Space Complexity:** `O(n²)`  
  - Due to the DP matrix.

---

## 🧩 Implementation

### problem_solution.py

```python
class Solution:
    def longest_palindromic_subsequence(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if i == j:
                    dp[i][j] = 1

                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

