# Longest Chain of Pairs (Dynamic Programming)

## 📌 Problem Description

Given a list of pairs, find the length of the longest chain that can be formed.

A pair `(a, b)` can be followed by another pair `(c, d)` **if and only if**: b < c


---

## 🧠 Approach

This solution uses **Dynamic Programming**.

### Steps:
1. Sort the pairs based on their first value.
2. Use a DP array where:
   - `dp[i]` represents the longest chain ending at index `i`.
3. For each pair, check all previous pairs and update the chain length.
4. Keep track of the maximum chain length.

---
## ⏱️ Complexity Analysis
1. Time Complexity: `O(n²) — due to nested loops after sorting`
2. Space Complexity: `O(n) — for the dynamic programming table`
## ✅ Python Solution

```python
class Solution(object):
    def findLongestChain(self, pairs):
        if not pairs:
            return 0

        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        longest_chain = 1

        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            longest_chain = max(longest_chain, dp[i])

        return longest_chain
