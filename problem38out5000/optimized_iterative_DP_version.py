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
        n = 5 → Output: 8
        Ways:
            1. 1 + 1 + 1 + 1 + 1
            2. 1 + 1 + 1 + 2
            3. 2 + 2 + 1
            4. 1 + 1 + 2 + 1
            5. 1 + 2 + 2
            6. 1 + 2 + 1 + 1
            7. 2 + 1 + 1 + 1
            8. 2 + 1 + 2

        Approach:
        ---------
        - This is a **Dynamic Programming** solution using an **iterative bottom-up approach**.
        - Instead of storing all intermediate results (as in tabulation), we only keep
          track of the last two results, since each step only depends on the two previous steps.
        - Base cases:
            - n = 1 → 1 way
            - n = 2 → 2 ways
        - For each step `i` from 3 to n:
            ways(i) = ways(i-1) + ways(i-2)
          This works because you can reach step `i` either:
            - From step `i-1` by taking 1 step, OR
            - From step `i-2` by taking 2 steps.

        Time Complexity:
        ----------------
        O(n) → We compute each step's value exactly once.

        Space Complexity:
        -----------------
        O(1) → We use only a constant amount of extra space (two variables).

        :param n: int - Number of steps in the staircase
        :return: int - Number of distinct ways to climb to the top
        """

        # Base cases: If there are 1 or 2 steps, the number of ways equals n
        if n <= 2:
            return n

        # Variables to store ways for previous two steps
        previous = 1  # ways to climb (n-2)
        current = 2   # ways to climb (n-1)

        # Compute ways for steps 3 to n
        for _ in range(3, n + 1):
            next_way = previous + current
            previous = current
            current = next_way

        return current


# Test the solution
if __name__ == "__main__":
    test_solution = Solution()
    n = 5
    print(f"The ways we can climb climbStairs({n}) is", test_solution.climbStairs(n))
