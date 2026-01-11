# Sum of Minimum and Maximum Elements

## Problem Statement
Given an array `A` of size `N` containing integers, find the sum of the
minimum and maximum elements in the array.

🔗 Source:  
https://www.geeksforgeeks.org/problems/max-min/1

---

## Approach
1. Initialize both minimum and maximum values with the first element.
2. Traverse the array once:
   - Update minimum if a smaller element is found.
   - Update maximum if a larger element is found.
3. Return the sum of minimum and maximum.

---

## Example

**Input**
A = [1, 3, 4, 1] 
N = 4

**Output**
 5


---

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

---

## Implementation
See `problem_solution.py`
