class Solution(object):
    def fib(self, n):
        """
        Computes the nth Fibonacci number using bottom-up dynamic programming.

        📌 Why Bottom-Up DP?
        -----------------------------------
        - Avoids recursion and call stack overhead.
        - Solves the problem by building up the solution from the smallest subproblems.
        - Time Complexity: O(n)
        - Space Complexity: O(n) [can be optimized to O(1)]

        🔁 Strategy:
        Use a DP table to store results from the base cases upward (tabulation).
        This prevents redundant work and guarantees linear time performance.

        :param n: The position in the Fibonacci sequence (0-indexed)
        :type n: int
        :return: The nth Fibonacci number
        :rtype: int
        """

        # Base cases
        if n == 0 or n == 1:
            return n

        # Create a DP table to store Fibonacci values
        dp_table = [0] * (n + 1)
        dp_table[0] = 0
        dp_table[1] = 1

        # Build up the table iteratively
        for i in range(2, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

        return dp_table[n]


# 🧪 Test the solution
if __name__ == "__main__":
    test_solution = Solution()
    n = 6
    result = test_solution.fib(n)
    print(f"Fibonacci({n}) is {result}")  # Output: 8
