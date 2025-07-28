class Solution(object):
    def fib(self, n, ht={0: 0, 1: 1}):
        """
        Efficiently computes the nth Fibonacci number using recursion with memoization.

        📌 Why Memoization?
        Without memoization, the recursive approach recalculates the same values multiple times,
        resulting in exponential time complexity (O(2^n)). By storing already computed results
        in a hash table, we reduce the time complexity to O(n).

        ➕ Advantages:
        - Reduces time complexity from exponential to linear
        - Avoids redundant calculations
        - Demonstrates dynamic programming principles

        :param n: Index of Fibonacci number (non-negative integer)
        :type n: int
        :param ht: Dictionary to store previously computed results
        :type ht: dict
        :return: nth Fibonacci number
        :rtype: int
        """

        # Base Case: Return cached value if exists
        if n in ht:
            return ht[n]

        # Recursive Case with Memoization
        ht[n] = self.fib(n - 1, ht) + self.fib(n - 2, ht)
        return ht[n]


# 🔍 Test the optimized Fibonacci function
if __name__ == "__main__":
    test_solution = Solution()
    n = 4
    result = test_solution.fib(n)
    print(f"Fibonacci({n}) is {result}")  # Output: 3
