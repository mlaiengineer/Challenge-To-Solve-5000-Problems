# First and Last Occurrences of an Element

## Problem Description
Given a sorted array `arr` with possibly some duplicates, find the **first and last occurrences** of an element `x`.  
If `x` is not found, return `[-1, -1]`.

🔗 [Problem Source - GeeksForGeeks](https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1?page=2&category=Arrays&difficulty=Medium&sortBy=submissions)

---

## Examples

| Input | x | Output |
|-------|----|--------|
| `[1, 3, 5, 5, 5, 5, 67, 123, 125]` | 5 | `[2, 5]` |
| `[1, 3, 5, 5, 5, 5, 7, 123, 125]` | 7 | `[6, 6]` |
| `[1, 2, 3]` | 4 | `[-1, -1]` |

---

## My Approach

The idea is to use **two pointers traversing simultaneously** from both ends of the array:

- **Left pointer** (`i`) starts from index `0` and moves forward to find the **first occurrence** of `x`.
- **Right pointer** starts from the last index and moves backward to find the **last occurrence** of `x`.

In each iteration:
1. Check if `arr[left_pointer] == x` and first occurrence is not set yet → record it.
2. Check if `arr[right_pointer] == x` and last occurrence is not set yet → record it.
3. Once **both occurrences are found**, exit early to save unnecessary iterations.

This way, we avoid two separate passes over the array and find both occurrences in a **single pass**.

---

## Complexity Analysis

| | Complexity |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Project Structure
```
├── problem_solution.py   # Solution implementation
├── test_cases.py         # Test cases
└── README.md             # Project documentation
```

---

## How to Run
```bash
# Run the solution tests
python test_cases.py
```

---

## Constraints
- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i], x ≤ 10^9
```

