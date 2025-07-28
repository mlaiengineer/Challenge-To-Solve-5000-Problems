class Solution(object):
    def fib(self, n):
        """
        Computes the nth Fibonacci number using a space-optimized iterative approach.

        📌 Why This Method?
        ----------------------------------------
        - Time Complexity: O(n)
        - Space Complexity: O(1) ✅
        - Unlike the recursive or tabulated approaches, this solution uses only two variables
          to keep track of the last two Fibonacci numbers, making it highly efficient and
          memory-friendly.

        ➕ Ideal for scenarios where:
        - You're working with limited memory.
        - You need maximum performance for large `n`.
        - You want to demonstrate mastery of dynamic programming simplification.

        :param n: The position in the Fibonacci sequence (0-indexed)
        :type n: int
        :return: The nth Fibonacci number
        :rtype: int
        """

        # Base case
        if n == 0 or n == 1:
            return n

        previous, current = 0, 1  # Initial Fibonacci numbers: F(0) = 0, F(1) = 1

        # Iteratively update values
        for i in range(2, n + 1):
            next_val = previous + current
            previous = current
            current = next_val

        return current


# 🧪 Test the optimized solution
if __name__ == "__main__":
    test_solution = Solution()
    n = 6
    result = test_solution.fib(n)
    print(f"Fibonacci({n}) is {result}")  # Output: 8
