# 🗓️ Today’s Progress — 2025-12-02

Today I solved the LeetCode problem **“Max Consecutive Ones.”**  
The task is to find the longest streak of consecutive `1`s in a binary array.

---

## 🚀 Problem Summary

Given a binary array `nums` (containing only 0s and 1s), return the **maximum number of consecutive 1’s**.

### Example
Input: [1,1,0,1,1,1]

Output: 3


---

## 🧠 Approach

To solve this problem efficiently:

1. Iterate through the array once.
2. Maintain two variables:
   - `current_count` → tracks the current consecutive 1s streak.
   - `max_ones` → stores the longest streak found so far.
3. When encountering `1`, increment `current_count`.
4. When encountering `0`, reset `current_count` to zero.
5. Always update `max_ones` to track the maximum streak.

This is a classic sliding-window / streak-counting logic.

---

## ⏱️ Complexity Analysis

### **Time Complexity: O(n)**  
We traverse the list once.

### **Space Complexity: O(1)**  
Only a few integer variables are used.

---

## 🔗 Problem Source  
https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

---

## 🧩 Final Code

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_count = 0
        max_ones = 0

        for value in nums:
            if value == 1:
                current_count += 1
                max_ones = max(max_ones, current_count)
            else:
                current_count = 0

        return max_ones
