# 647. Palindromic Substrings — LeetCode

**Source:** https://leetcode.com/problems/palindromic-substrings/

## 🧠 Problem Description

Given a string `s`, return the number of **palindromic substrings** in it.

- A string is a palindrome when it reads the same backward as forward.
- A substring is a contiguous sequence of characters within the string.

### Examples

**Example 1**

Input:
s = "abc"

Output:
3  
Explanation: "a", "b", "c"

**Example 2**

Input:
s = "aaa"

Output:
6  
Explanation: "a", "a", "a", "aa", "aa", "aaa"

### Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

---

# ✅ Approach 1: Memoization (Top-Down Recursion)

### Idea
- Use recursion to check if substring `s[i:j]` is a palindrome.
- Store results in a memo table to avoid recomputation.

### Complexity
- **Time:** O(n²) — each substring checked once  
- **Space:** O(n²) — memo table + recursion stack

### Implementation

```python
class Solution(object):
    def countSubstrings(self, s):
        n = len(s)

        # memo[i][j] -> whether substring s[i:j+1] is palindrome
        memo = [[None] * n for _ in range(n)]

        def is_palindrome(left, right):
            if left >= right:
                return True

            if memo[left][right] is not None:
                return memo[left][right]

            memo[left][right] = (
                s[left] == s[right] and is_palindrome(left + 1, right - 1)
            )
            return memo[left][right]

        count = 0
        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    count += 1

        return count
```

---

# ✅ Approach 2: Tabulation (Bottom-Up DP)

### Idea
- Build a 2D table `dp[i][j]` representing whether substring `s[i:j]` is palindrome.
- Expand by length from 1 → n.

### Complexity
- **Time:** O(n²)  
- **Space:** O(n²)

### Implementation

```python
class Solution(object):
    def countSubstrings(self, s):
        n = len(s)

        # dp[i][j] = True if substring s[i:j] is palindrome
        dp = [[False] * n for _ in range(n)]

        result = 0

        # l = length of substring
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if i == j:
                    dp[i][j] = True

                elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                if dp[i][j]:
                    result += 1

        return result
```

---

# 🧪 Test Cases

```python
def test_countSubstrings():
    solution = Solution()

    # Basic tests
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6

    # Additional tests
    assert solution.countSubstrings("aba") == 4
    assert solution.countSubstrings("abba") == 6
    assert solution.countSubstrings("a") == 1

    print("All test cases passed ✅")

if __name__ == "__main__":
    test_countSubstrings()
```

---

# 📊 Comparison of Approaches

| Approach     | Time | Space | Style |
|---------------|------|-------|-------|
| Memoization   | O(n²)| O(n²) | Top-Down |
| Tabulation    | O(n²)| O(n²) | Bottom-Up |


---

## 📌 Notes

- Both solutions are efficient for `n ≤ 1000`.
- Tabulation is iterative and usually faster in practice.
- Memoization is easier to write recursively.

---
