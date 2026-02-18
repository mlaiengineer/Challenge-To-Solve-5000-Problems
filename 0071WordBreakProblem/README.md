# 139. Word Break

## Problem Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

> Note: The same word in the dictionary may be reused multiple times in the segmentation.

**Platform:** [LeetCode](https://leetcode.com/problems/word-break/description/)  
**Difficulty:** Medium  
**Category:** Dynamic Programming / Recursion

---

## Examples

**Example 1:**
```
Input:  s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".
```

**Example 2:**
```
Input:  s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: "applepenapple" can be segmented as "apple pen apple".
             Note that dictionary words can be reused.
```

**Example 3:**
```
Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
Explanation: "catsandog" cannot be fully segmented using dictionary words.
```

---

## Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All strings of `wordDict` are unique.

---

## My Approach

1. Used a **recursive approach** with a helper function `check(index)` that starts from index `n - 1` (last character of the string).
2. At each index, iterate through every word in the dictionary and check if the substring ending at that index matches the word.
3. If a match is found, recursively check the remaining part of the string before that word.
4. **Base case:** if `index < 0`, the entire string has been successfully segmented, return `True`.
5. If no word matches at the current index, return `False`.

---

## Solution

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)                                          # Store the total length of the input string
        
        def check(index):
            
            # Base case: index is negative, entire string is segmented successfully
            if index < 0:
                return True
            
            # Try every word in the dictionary at the current index
            for word in wordDict:
                word_length = len(word)                     # Get the length of the current dictionary word
                start = index - word_length                 # Calculate the starting index of the substring
                substring = s[start: index + 1]            # Extract substring matching the current word length
                
                if substring == word and check(index - word_length):   # Check if substring matches word and recurse
                    return True
            
            return False                                    # No word matched at this index, return False
        
        return check(n - 1)                                # Start checking from the last index of the string
```

---

## Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| **Time** | O(2^n) | Each index can branch into multiple recursive calls without memoization |
| **Space** | O(n) | Recursive call stack depth can go up to n levels |

> ⚠️ **Note:** This solution may hit **Time Limit Exceeded (TLE)** on LeetCode for large inputs due to overlapping subproblems. It can be optimized using **memoization** (Top-Down DP) or **Bottom-Up DP** to bring time complexity down to **O(n² × m)** where m is the average word length.

---

## Key Takeaway

This problem is a great example of how **recursion** can naturally model string segmentation problems. However, without memoization, repeated subproblems cause exponential time complexity — making it a perfect candidate for **Dynamic Programming** optimization.
