   class Solution(object):
    def climbStairs(self, n, ht={1: 1, 2: 2}):
        """
        Problem:
        --------
        You are climbing a staircase with `n` steps.
        Each time, you can climb either 1 step or 2 steps.
        The task is to find how many distinct ways you can reach the top.

        Example:
        --------
        n = 3 → Output: 3
        Ways:
            1. 1 + 1 + 1
            2. 1 + 2
            3. 2 + 1

        Approach:
        ---------
        - This is a classic **Dynamic Programming** problem.
        - I use **Memoization** to store already computed results
          to avoid recalculating subproblems.
        - Base cases:
            - n = 1 → 1 way
            - n = 2 → 2 ways
        - Recursive relation:
            f(n) = f(n-1) + f(n-2)

        Optimization:
        -------------
        - I store results in a dictionary (`ht`) to avoid repeated calculations.
        - This improves performance drastically from exponential to linear.

        Time Complexity:
        ----------------
        O(n) → Each value from 1 to n is computed only once.

        Space Complexity:
        -----------------
        O(n) → For storing results in the hash table and recursion stack.

        :param n: int - Number of steps in the staircase
        :param ht: dict - Memoization table to store computed values
        :return: int - Number of distinct ways to climb to the top
        """

        # If already computed, return stored result (memoization)
        if n in ht:
            return ht[n]

        # Compute and store result for current n
        ht[n] = self.climbStairs(n - 1, ht) + self.climbStairs(n - 2, ht)

        return ht[n]


# Test the solution
if __name__ == "__main__":
    test_solution = Solution()
    n = 5
    print(f"The ways we can climb climbStairs({n}) is", test_solution.climbStairs(n))
