# 5. Longest Palindromic Substring — LeetCode

**Source:**  
https://leetcode.com/problems/longest-palindromic-substring/

---

## 🧠 Problem Description

Given a string `s`, return **the longest palindromic substring** in `s`.

A string is a palindrome when it reads the same backward as forward.

### Examples

**Example 1**

Input:
s = "babad"

Output:
"bab"

Explanation: "aba" is also a valid answer.

---

**Example 2**

Input:
s = "cbbd"

Output:
"bb"

---

### Constraints

- 1 <= s.length <= 1000  
- s consists of only digits and English letters.

---

# 📁 Project Structure

0064LongestPalindromicSubstringProblem/
├── solution_using_tabulation.py
├── test_longestPalindrome.py
└── README.md


---

# ✅ Approach — Tabulation (Bottom-Up DP)

### Idea

- Use a 2D table `dp[i][j]`
- `dp[i][j] = True` → substring `s[i:j+1]` is palindrome
- Build table by increasing substring length

### Transition

- Single character → palindrome  
- Two characters → check equality  
- More → check: `s[i] == s[j] AND dp[i+1][j-1] == True`

---

## ⏱ Complexity Analysis

- **Time Complexity:** O(n²)  
- **Space Complexity:** O(n²)

---

# 💻 Implementation

### solution_using_tabulation.py

```python
class Solution(object):
  def longestPalindrome(self, s):
      n = len(s)

      dp = [[False] * n for _ in range(n)]
      longest = s[0]

      for length in range(1, n + 1):
          for i in range(n - length + 1):
              j = i + length - 1

              if i == j:
                  dp[i][j] = True

              elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                  dp[i][j] = True

              if dp[i][j] and length > len(longest):
                  longest = s[i:j + 1]

      return longest
