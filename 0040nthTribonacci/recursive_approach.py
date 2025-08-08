class Solution(object):
    def tribonacci(self, n):
        """
        Calculate the n-th Tribonacci number using recursion.

        The Tribonacci sequence is a generalization of the Fibonacci sequence where each term
        is the sum of the three preceding ones. It starts as:
        T(0) = 0, T(1) = 1, T(2) = 1, T(3) = 2, T(4) = 4, T(5) = 7, T(6) = 13, ...

        Parameters:
            n (int): The index (n >= 0) of the Tribonacci number to compute.

        Returns:
            int: The n-th Tribonacci number.

        Time Complexity:
            O(3^n) – Each function call leads to 3 recursive calls in the worst case,
            resulting in exponential growth in the number of calls.

        Space Complexity:
            O(n) – Due to the maximum depth of the recursive call stack.
        """
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Recursive case: T(n) = T(n-1) + T(n-2) + T(n-3)
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


# ------------------------------
# Example usage and test cases
# ------------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Known output for n = 4 -> T(4) = 4
    assert solution.tribonacci(4) == 4, "Test Case 1 Failed"

    # Test Case 2: Known output for n = 6 -> T(6) = 13
    assert solution.tribonacci(6) == 13, "Test Case 2 Failed"

    print("All test cases passed.")
