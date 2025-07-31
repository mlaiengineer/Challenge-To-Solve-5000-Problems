class Solution(object):
    def climbStairs(self, n):
        """
        Problem:
        --------
        You are climbing a staircase. It takes `n` steps to reach the top.
        Each time, you can either climb 1 step or 2 steps.
        The task is to determine how many distinct ways you can climb to the top.

        Example:
        --------
        n = 3 → Output: 3
        Explanation:
            1 step + 1 step + 1 step
            1 step + 2 steps
            2 steps + 1 step

        Approach:
        ---------
        - This solution uses recursion to solve the problem.
        - Base case: If `n` is 1 → 1 way; if `n` is 2 → 2 ways.
        - Recursive relation: f(n) = f(n-1) + f(n-2)
          This is because you can reach step `n` either:
            - From step `n-1` by taking 1 step, OR
            - From step `n-2` by taking 2 steps.

        Time Complexity:
        ----------------
        O(2^n) → Because at each step, we branch into 2 recursive calls.
        This grows exponentially as `n` increases.

        Space Complexity:
        -----------------
        O(n) → Due to the recursion call stack, which at most goes `n` levels deep.

        :param n: int - Number of steps in the staircase
        :return: int - Number of distinct ways to climb to the top
        """

        # Base case: If there are 1 or 2 steps, the number of ways equals n
        if n <= 2:
            return n

        # Recursive case: Sum of ways from (n-1) and (n-2) steps
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Test the solution
if __name__ == "__main__":
    test_solution = Solution()
    n = 5
    print(f"The ways we can climb climbStairs({n}) is", test_solution.climbStairs(n))
