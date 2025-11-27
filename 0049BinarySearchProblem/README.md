# 🔎 Binary Search: Finding the First Occurrence

## ✨ Summary

This repository presents an **efficient implementation of Binary Search** designed to find the **first (smallest) index** of a target value (`k`) within a **sorted array**. The solution optimizes for speed, achieving a **logarithmic time complexity** of $O(\log N)$, which is significantly faster than the linear $O(N)$ time complexity of a standard linear search. This specific variation ensures that if a target value appears multiple times, the index of its leftmost occurrence is returned.

---

### 📝 Problem Description

Given a **sorted array** `arr[]` and an integer target value `k`, the goal is to find the position (0-based index) at which `k` is present in the array using **Binary Search**.

* If `k` is not found in the array, the function must return **-1**.
* **Crucial Note:** If there are **multiple occurrences** of `k`, the function must return the **smallest index** (the leftmost occurrence).

| Example Array | Target `k` | Smallest Index (Result) |
| :------------ | :--------- | :---------------------- |
| `[1, 2, 2, 4, 5]` | `2` | `1` |
| `[10, 20, 30]` | `30` | `2` |
| `[1, 5, 8]` | `6` | `-1` |

---

### 🔗 Problem Source

This problem is adapted from the following resource:
* **GeeksforGeeks:** [Binary Search](https://www.geeksforgeeks.org/problems/binary-search-1587115620/1?page=1&sortBy=submissions)

---

### 💡 Why Binary Search?

Binary Search is a highly efficient searching algorithm that operates exclusively on **sorted data**. It achieves its speed by repeatedly dividing the search interval in half. This makes it ideal for performance-critical applications.

#### Time Complexity

| Algorithm | Worst-Case Time Complexity | Rationale |
| :-------- | :------------------------- | :-------- |
| **Binary Search** | $O(\log N)$ | The search space is halved in every iteration. |
| **Linear Search** | $O(N)$ | Requires checking up to $N$ elements in the worst case. |

#### Space Complexity

The implementation provided uses an iterative approach, achieving optimal space efficiency.

* **Space Complexity (Iterative):** $O(1)$ (Constant extra space, regardless of array size).

---

### 🚀 Implementation Details (Python)

The key modification to the standard Binary Search is made when an occurrence of `k` is found:

1.  We store the current `mid` index as a potential result.
2.  Instead of stopping, we immediately narrow the search space to the left side (`high = mid - 1`). This forces the algorithm to continue searching for an *even smaller* index that might also contain `k`, thus guaranteeing the smallest index is ultimately returned.

---

### 📚 How This Problem Helps

Mastering this variation of Binary Search (finding the first occurrence) is a fundamental skill in algorithm design and a common interview question. It helps to:

* **Reinforce Binary Search Mechanics:** Understand how to manipulate the `low` and `high` pointers to find not just a value, but a specific boundary (the *first* instance).
* **Differentiate Search Algorithms:** Clearly see the performance difference between $O(\log N)$ and $O(N)$ complexity, allowing you to choose the optimal search method for sorted data.
* **Build Foundational Skills:** This concept is a crucial building block for more complex algorithms that involve range finding or "search space reduction."