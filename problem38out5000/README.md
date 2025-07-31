# 🧗‍♂️ Climbing Stairs – Multiple Solutions in Python

## 📌 Problem Statement
You are climbing a staircase with `n` steps.  
Each time, you can climb **either 1 step or 2 steps**.  
Your task is to determine **how many distinct ways** you can climb to the top.

---

## 📝 Example
**Input:**
n = 5
**Output:**
8
**Explanation:**
Ways to climb 5 steps:
1. 1 + 1 + 1 + 1 + 1  
2. 1 + 1 + 1 + 2  
3. 1 + 1 + 2 + 1  
4. 1 + 2 + 1 + 1  
5. 2 + 1 + 1 + 1  
6. 1 + 2 + 2  
7. 2 + 2 + 1  
8. 2 + 1 + 2  

---

## 🔍 Approaches

### 1️⃣ Recursive Solution
- Uses **brute force recursion**.
- Directly applies the recurrence relation:
f(n) = f(n-1) + f(n-2)
- Simple to implement but **very slow** for large `n`.

**Time Complexity:** O(2^n)  
**Space Complexity:** O(n) (recursion stack)

---

### 2️⃣ Memoization (Top-Down Dynamic Programming)
- Improves recursion by **storing previously computed results** in a hash table.
- Avoids recalculating subproblems.

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (memo table + recursion stack)

---

### 3️⃣ Tabulation (Bottom-Up Dynamic Programming)
- Builds results from the smallest subproblems up to `n`.
- Uses a **DP array** to store all intermediate values.

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (DP array)

---

### 4️⃣ Iterative DP with O(1) Space (Optimal)
- Stores only the **last two results** instead of the whole DP table.
- Most **memory-efficient** solution.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## 📊 Time & Space Complexity Summary

| Approach                | Time Complexity | Space Complexity | Notes |
|-------------------------|----------------|----------------|-------|
| Recursive               | O(2^n)         | O(n)           | Exponential growth – inefficient |
| Memoization (Top-Down)  | O(n)           | O(n)           | Stores computed results |
| Tabulation (Bottom-Up)  | O(n)           | O(n)           | Builds from smallest subproblem |
| Iterative O(1) Space    | O(n)           | O(1)           | Most efficient |

---
📚 Related Topics
Dynamic Programming

Recursion

Fibonacci Sequence

