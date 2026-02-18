# Count Even Letters

## Problem Description

Given a string `s` consisting of lowercase English letters, count how many distinct characters appear an **even number of times** in the string.

**Platform:** [GeeksForGeeks](https://www.geeksforgeeks.org/problems/count-even-letters/1?page=8&category=Strings&difficulty=Easy&status=unsolved&sortBy=submissions)  
**Difficulty:** Easy  
**Category:** Strings

---

## Examples

**Example 1:**
```
Input:  s = "abacaba"
Output: 2
Explanation: a appears 4 times, b appears 2 times, c appears 1 time.
             So 2 characters (a, b) have even frequency.
```

**Example 2:**
```
Input:  s = "zzacccz"
Output: 0
Explanation: z appears 3 times, a appears 1 time, c appears 3 times.
             No characters have even frequency.
```

---

## Constraints

- `1 ≤ s.size() ≤ 10^5`

---

## My Approach

1. Initialize a counter variable `even_count` to track how many characters appear an even number of times.
2. Use a **dictionary** data structure where each character is stored as a key and its frequency as the value.
3. Iterate through the string, building the frequency map for each character.
4. Loop through the dictionary and check if each frequency is even using the modulo operator `% 2 == 0`.
5. If the condition is true, increment `even_count`.
6. Finally, return `even_count`.

---

## Solution

```python
class Solution:
    def count(self, s):
        
        even_count = 0                          # Tracks number of characters with even frequency
        char_frequency = {}                     # Maps each character to its occurrence count
        
        for char in s:
            if char not in char_frequency:
                char_frequency[char] = 1        # Initialize character frequency to 1 on first encounter
            else:
                char_frequency[char] += 1       # Increment frequency for already seen character
        
        for char, frequency in char_frequency.items():
            if frequency % 2 == 0:              # Check if character frequency is divisible by 2
                even_count += 1                 # Increment counter if frequency is even
        
        return even_count                       # Return total distinct characters with even frequency
```

---

## Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | Iterating through the string once to build the frequency map |
| **Space** | O(n) | Dictionary stores at most n distinct characters |

---

## Key Takeaway

Using a **dictionary** to store character frequencies is an efficient and clean approach for this type of problem, allowing a single pass to build the map and a second pass to evaluate the condition.
