# 📈 Longest Increasing Subsequence (LIS)

## 📌 Problem Description

Given an integer array `nums`, return the **length of the longest strictly increasing subsequence**.

A subsequence is derived by deleting some or no elements **without changing the order** of the remaining elements.

### Examples

Input: [10,9,2,5,3,7,101,18]


Output: 4


Explanation: The LIS is [2,3,7,101]

---

## 🔗 Problem Source

LeetCode — Problem 300  
https://leetcode.com/problems/longest-increasing-subsequence/description/

---

## 🚀 Approach Used (Binary Search / Patience Sorting)

This solution uses an **optimized O(n log n)** approach:

### Key Idea
- Maintain an array `sub` where:
  - `sub[i]` represents the **smallest possible tail value** of an increasing subsequence of length `i + 1`.

### Steps
1. Initialize `sub` with the first element.
2. For each number in the array:
   - If the number is greater than the last element in `sub`, append it.
   - Otherwise, use **binary search** to find the correct index and replace the value.
3. The length of `sub` at the end is the length of the LIS.

⚠️ Note:  
`sub` does **not** store the actual LIS — it only tracks lengths efficiently.

---

## ⏱️ Complexity Analysis

### **Time Complexity: O(n log n)**
- Each element is processed once.
- Binary search is performed in `log n`.

### **Space Complexity: O(n)**
- Extra array `sub` is used to store potential subsequence tails.

---

## 🧩 Final Code

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        def binary_search(sub, num):
            left, right = 0, len(sub) - 1
            while left < right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left

        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                sub[binary_search(sub, num)] = num

        return len(sub)
