# Reverse Each Word in a Given String

## Problem Description

Given a string `s`, reverse each word in it where the words are separated by spaces and return the modified string.

> Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string should only have a single space separating the words, and no extra spaces should be included.

**Platform:** [GeeksForGeeks](https://www.geeksforgeeks.org/problems/reverse-each-word-in-a-given-string1001/1?page=2&category=Strings&difficulty=Medium&status=unsolved&sortBy=submissions)  
**Difficulty:** Medium  
**Category:** Strings

---

## Examples

**Example 1:**
```
Input:  s = " i like this program very much "
Output: "i ekil siht margorp yrev hcum"
Explanation: Each word is reversed individually:
             "i"->"i", "like"->"ekil", "this"->"siht",
             "program"->"margorp", "very"->"yrev", "much"->"hcum"
```

**Example 2:**
```
Input:  s = " pqr mno "
Output: "rqp onm"
Explanation: "pqr"->"rqp", "mno"->"onm"
```

**Example 3:**
```
Input:  s = "pqr"
Output: "rqp"
Explanation: "pqr"->"rqp"
```

---

## Constraints

- `1 <= s.size() <= 10^5`
- String `s` contains only lowercase English alphabets and spaces.

---

## My Approach

1. Use Python's `split()` method to split the string into a list of words — this automatically handles leading, trailing, and multiple spaces between words.
2. Iterate through each word using a `for` loop and reverse it using slicing `word[::-1]`.
3. Accumulate each reversed word into the result string with a trailing space.
4. Finally, return the result using `strip()` to remove the extra trailing space.

---

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()          # Split string into words, handles all extra spaces automatically
        reversed_s = ''                 # Initialize empty string to accumulate reversed words

        for word in words_list:
            reversed_s += word[::-1] + ' '  # Reverse each word and append with a space

        return reversed_s.strip()       # Remove trailing space before returning
```

---

## Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | Iterating through all characters in the string once |
| **Space** | O(n) | Storing the split words list and the result string |

---

## Key Takeaway

Python's `split()` method is very powerful — with no arguments it splits on any whitespace
and automatically removes leading, trailing, and multiple spaces, eliminating
the need for manual trimming before processing. Combined with slicing 
`[::-1]` for reversing, this leads to a clean and concise solution.