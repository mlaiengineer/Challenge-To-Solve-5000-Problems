# **0048 FizzBuzz Problem**

## 📝 Problem Description

Given an integer n, the task is to return an array of strings representing the numbers from 1 to n. The numbers must be replaced with specific keywords based on divisibility:

Numbers that are multiples of 3 should be replaced with "Fizz".

Numbers that are multiples of 5 should be replaced with "Buzz".

Numbers that are multiples of both 3 and 5 (i.e., multiples of 15) should be replaced with "FizzBuzz".

Numbers that are not multiples of 3 or 5 should be represented as their string equivalent.

Source: [freeCodeCamp Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-25)

#### 📊 Complexity Analysis

The solution uses a single loop that iterates from 1 up to n. Inside the loop, only constant-time arithmetic operations (modulo, comparison, and string concatenation) are performed.

#### Time Complexity: O(n)

The algorithm performs a constant number of operations for each of the n iterations in the loop. Therefore, the total time required is directly proportional to the input size n.

#### Space Complexity: O(1) or O(n)

O(n) (Output Space): If we count the space required to store the output array of size n (which is necessary for the problem's requirement), the space complexity is O(n).

O(1) (Auxiliary Space): If we only consider the extra space used by variables during the computation (excluding the storage for the final output array), the auxiliary space complexity is O(1).