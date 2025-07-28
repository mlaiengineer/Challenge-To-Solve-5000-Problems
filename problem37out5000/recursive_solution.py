class Solution(object):
    def fib(self, n):
        """
        Recursive function to calculate the nth Fibonacci number.

        The Fibonacci sequence is a series of numbers in which each number
        is the sum of the two preceding ones, usually starting with 0 and 1.

        Time Complexity: O(2^n) due to repeated calculations.
        Space Complexity: O(n) due to recursive call stack.

        :param n: Index of Fibonacci number (non-negative integer)
        :type n: int
        :return: nth Fibonacci number
        :rtype: int
        """

        # Base case: If n is 0 or 1, return n directly
        if n == 0 or n == 1:
            return n

        # Recursive case: sum of the previous two Fibonacci numbers
        return self.fib(n - 1) + self.fib(n - 2)


# 🔍 Test the recursive Fibonacci implementation
if __name__ == "__main__":
    test_solution = Solution()
    n = 4
    result = test_solution.fib(n)
    print(f"Fibonacci({n}) = {result}")  # Expected output: 3

    # Breakdown:
    # fib(4) = fib(3) + fib(2)
    #        = (fib(2) + fib(1)) + (fib(1) + fib(0))
    #        = (1 + 1) + (1 + 0) = 3
