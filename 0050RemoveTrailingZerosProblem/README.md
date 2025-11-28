## 🚀 Remove Trailing Zeros From a String

This repository contains a solution to the LeetCode problem **2710. Remove Trailing Zeros From a String**.

The goal is to take a string representation of a positive integer and return a new string with all trailing zeros removed.

### 🔗 Problem Source

[LeetCode: Remove Trailing Zeros From a String](https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/)

***

## 🎯 Algorithm: Reverse Traversal and Slicing

The solution employs a straightforward **iterative approach** by traversing the input string from right to left (end to beginning).

### 💡 Step-by-Step Logic

1.  **Reverse Traversal:** Start an iteration loop from the **last index** of the input string (`num`) and move backward toward the beginning.
2.  **Find the Stop Point:** In each step, check the current character.
    * If the character is a **non-zero digit** (`'1'` through `'9'`), this is the **last significant digit**. We stop the traversal here and record its index.
    * If the character is a **zero** (`'0'`), it is a trailing zero, and we continue the traversal to the next position to the left.
3.  **Determine the Result:** Once the last non-zero digit is found at index $i$, the final result is the **substring** of the original input from the start (index 0) **up to and including** index $i$.
4.  **Handling No Zeros:** If the loop finishes without finding any zeros (i.e., the string has no trailing zeros), the result is the original string itself.

***

## 💻 Technical Analysis

### Time Complexity

The algorithm iterates through the string from the end to the start at most once. The time taken is directly proportional to the length of the string $N$.

* **Time Complexity: $O(N)$**
    * Where $N$ is the length of the input string `num`.

### Space Complexity

The solution only uses a few variables to store the index and perform the slicing.

* **Space Complexity: $O(1)$**
    * The solution uses a constant amount of extra space, regardless of the input size.

***

## 🧠 Personal Learning Benefits

Solving this problem offered valuable practice in fundamental programming concepts, specifically:

* **Mastering Reverse Iteration:** It reinforced the logic for configuring a **`for` loop** to effectively traverse a sequence (like a string) from the **end to the beginning**.
* **Improving String Manipulation:** It provided practical experience in using **string slicing** in Python to efficiently extract the necessary part of the string once the correct boundaries are determined.
* **Enhancing Logical Thinking:** The exercise required developing a precise and efficient **logical condition** to determine the exact cutoff point for removing the trailing zeros, thus improving overall problem-solving skills.