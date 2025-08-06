# 🧗‍♀️ Problem 39 of 5000: Minimum Cost to Climb Stairs  

## 📝 Problem Description  
You are given an integer array `cost` where `cost[i]` is the cost of the `i-th` step on a staircase.  
Once you pay the cost, you can either:  
1️⃣ Climb **1 step** or  
2️⃣ Climb **2 steps**.

You can start at either step **index 0** or **index 1**. Return the **minimum cost** to reach the top of the floor.  

---

### 🧮 Example:  

#### Example 1:  
**Input:**  
```python
cost = [10, 15, 20]

🚀 Solutions
Approach #1: Recursive Solution
Description:
A simple recursive approach that explores all possible paths by trying to jump 1 or 2 steps at each point.

Time Complexity:
O(2^n) - Exponential as it explores all possible paths.

Space Complexity:
O(n) - Due to the recursion stack.

Approach #2: Memoization (Top-Down)
Description:
Optimized recursive solution using memoization to store results of subproblems and avoid redundant calculations.

Time Complexity:
O(n) - Each step is computed only once.

Space Complexity:
O(n) - Extra space for memoization and recursion stack.

Approach #3: Dynamic Programming (Bottom-Up)
Description:
Iterative approach using a DP array to build the solution from the base case to the final result.

Time Complexity:
O(n) - Each step is processed once.

Space Complexity:
O(n) - Space for the DP array.
🧠 Key Takeaways
Dynamic programming transforms exponential problems into polynomial-time solutions.
Space optimization can significantly reduce memory usage in iterative solutions.

- README.md       # Problem description and solution approaches  
- solutions/      # Folder containing Python solution files  
  ├── recursive.py  
  ├── memoization.py  
  ├── dp_bottom_up.py  
  ├── dp_optimized.py

Feel free to adjust links or add your personal touch to make it even more aligned with your style! 😊

