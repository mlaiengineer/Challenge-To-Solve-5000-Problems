class Solution(object):
    def climbStairs(self, n):
        """
        Problem:
        --------
        You are climbing a staircase with `n` steps.
        Each time, you can climb either 1 step or 2 steps.
        The task is to find how many distinct ways you can reach the top.

        Example:
        --------
        n = 4 → Output: 5
        Ways:
            1. 1 + 1 + 1 + 1
            2. 1 + 1 + 2
            3. 2 + 2
            4. 1 + 2 + 1
            5. 2 + 1 + 1

        Approach:
        ---------
        - This solution uses **Dynamic Programming** with **Tabulation** (bottom-up).
        - We start from the smallest subproblems and build up to the final result.
        - Base cases:
            - n = 1 → 1 way
            - n = 2 → 2 ways
        - For each step `i`, the total ways = ways to reach (i-1) + ways to reach (i-2)
        - This works because you can reach step `i` either:
            - From step `i-1` by taking 1 step, OR
            - From step `i-2` by taking 2 steps.

        Time Complexity:
        ----------------
        O(n) → We calculate the number of ways for each step from 3 to n exactly once.

        Space Complexity:
        -----------------
        O(n) → We store results for all steps in a DP table.

        :param n: int - Number of steps in the staircase
        :return: int - Number of distinct ways to climb to the top
        """

        # Base case: For 1 or 2 steps, ways = n
        if n <= 2:
            return n

        # Create a DP table to store results for subproblems
        dp_table = [0] * (n + 1)

        # Base cases
        dp_table[1] = 1
        dp_table[2] = 2

        # Fill the DP table for steps 3 to n
        for i in range(3, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

        return dp_table[n]


# Test the solution
if __name__ == "__main__":
    test_solution = Solution()
    n = 4
    print(f"The ways we can climb climbStairs({n}) is", test_solution.climbStairs(n))
