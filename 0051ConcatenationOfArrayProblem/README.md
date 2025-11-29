# Concatenation of Array (LeetCode 1929) 🧩

## 🔗 Problem Source

**LeetCode:** [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i)

---

## 📝 Problem Description

Given an integer array `nums` of length $n$, the goal is to create a new array, `ans`, of length $2n$.

The array `ans` must be the **concatenation** of two copies of the `nums` array. This is formally defined by the conditions:
* $ans[i] = nums[i]$ for $0 \le i < n$
* $ans[i + n] = nums[i]$ for $0 \le i < n$

In simple terms: $\text{ans} = \text{nums} + \text{nums}$.

### Examples

| Input (`nums`) | Output (`ans`) |
| :------------- | :------------- |
| `[1, 2, 1]`    | `[1, 2, 1, 1, 2, 1]` |
| `[1, 3, 2, 1]` | `[1, 3, 2, 1, 1, 3, 2, 1]` |

---

## 🧠 Algorithm: Modulo Indexing Approach

This solution utilizes an iterative approach with **modulo arithmetic** to efficiently map the index of the resultant array (`ans`) back to the correct index in the original array (`nums`).

### Summary of the Algorithm

1.  **Initialization:** The length of the input array, $n$, is calculated. A new array, `ans`, is **pre-allocated** with a size of $2n$.
2.  **Iteration:** A single loop iterates through every index $i$ of the new array `ans`, from $0$ up to $2n - 1$.
3.  **Mapping with Modulo:** Inside the loop, the value for $ans[i]$ is determined by $nums[i \pmod n]$.
    * **First Half ($0 \le i < n$):** When $i < n$, $i \pmod n$ simply equals $i$. This correctly populates the first copy of `nums`.
    * **Second Half ($n \le i < 2n$):** When $i \ge n$, $i \pmod n$ effectively calculates $i - n$. This correctly cycles back through the indices $0$ to $n-1$, populating the second copy of `nums`.
4.  **Return:** The completely populated array `ans` is returned.

### Implementation Snippet (Python)

```python
class Solution(object):
    def getConcatenation(self, nums):
        """
        Calculates the concatenation of an array with itself using modulo indexing.
        """
        n = len(nums)
        # 1. Initialize the result array 'ans' with a length of 2n
        ans = [0] * (n * 2)
        
        # 2. Iterate and map the index using the modulo operator
        for i in range(len(ans)):
            # ans[i] corresponds to nums[i % n]
            ans[i] = nums[i % n] 
            
        return ans