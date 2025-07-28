📝 Problem Description
The Fibonacci Sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. Mathematically:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Task:
Given a non-negative integer n, calculate the nth Fibonacci number.

Example
Input:
n = 2  
Output:
1
Explanation:
F(2) = F(1) + F(0) = 1 + 0 = 1

🚀 Solution Approaches
This repository contains four different approaches to solving the Fibonacci sequence problem, each with its unique trade-offs in terms of time and space complexity.

1️⃣ Recursive Approach
Description: A straightforward recursive solution following the mathematical definition.
Time Complexity: O(2^n) (due to repeated calculations).
Space Complexity: O(n) (call stack).
Code: Recursive Solution

2️⃣ Recursive with Memoization (Dynamic Programming)
Description: Optimizes the basic recursive solution by storing already computed results (memoization).
Time Complexity: O(n) (avoids redundant calculations).
Space Complexity: O(n) (for the memoization table).
Code: Memoization Solution

3️⃣ Bottom-Up Dynamic Programming (Tabulation)
Description: Builds up the solution iteratively using a table to store results of subproblems.
Time Complexity: O(n)
Space Complexity: O(n) (for the DP table).
Code: Tabulation Solution

4️⃣ Space-Optimized Iterative Approach
Description: Uses two variables to store the last two Fibonacci numbers instead of a full table, reducing space usage.
Time Complexity: O(n)
Space Complexity: O(1)
Code: Optimized Iterative Solution

📂 Repository Structure

📁 problem37out5000

├── recursive_solution.py  
├── memoization_solution.py  
├── tabulation_solution.py  
├── optimized_iterative_solution.py  
└── README.md

🔗 Resources
Fibonacci Sequence on Wikipedia
Dynamic Programming Principles

💡 Key Takeaways
Recursive solutions are simple but inefficient for large inputs.
Dynamic programming (memoization and tabulation) drastically improves performance.
Space optimization is essential for memory-constrained environments.

🛠️ How to Run the Solutions
git clone https://github.com/mlaiengineer/problem37out5000.git  
cd problem37out5000

Run any of the solution files:
python recursive_solution.py
