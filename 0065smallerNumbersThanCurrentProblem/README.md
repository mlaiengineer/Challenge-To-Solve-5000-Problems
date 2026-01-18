# 1365. How Many Numbers Are Smaller Than the Current Number

**Source:**  
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

---

## 🧠 Problem Description

Given the array `nums`, for each `nums[i]` find out how many numbers in the array are **smaller than it**.

For each index `i`, count the number of valid indices `j` such that:

- `j != i`
- `nums[j] < nums[i]`

Return the answer as an array.

---

### Examples

#### Example 1
Input:
nums = [8,1,2,2,3]

Output:
[4,0,1,1,3]

Explanation:  
- For 8 → four numbers are smaller (1,2,2,3)  
- For 1 → none  
- For 2 → one (1)  
- For 3 → three (1,2,2)

---

#### Example 2
Input:
nums = [6,5,4,8]

Output:
[2,1,0,3]

---

#### Example 3
Input:
nums = [7,7,7,7]

Output:
[0,0,0,0]

---

### Constraints

- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`

---

---

# ✅ Approach — Brute Force

### Idea

For each element:

1. Compare it with every other element  
2. Count how many are strictly smaller  
3. Store result in output array

---

## ⏱ Complexity Analysis

- **Time Complexity:** O(n²)  
- **Space Complexity:** O(n)

---

# 💻 Implementation

### solution.py

```python
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        For each element in the array, count how many numbers
        are strictly smaller than it.

        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):
            current_value = nums[i]
            smaller_count = 0

            for j in range(len(nums)):
                if nums[j] < current_value:
                    smaller_count += 1

            result.append(smaller_count)

        return result


