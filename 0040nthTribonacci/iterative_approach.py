class Solution(object):
    def tribonacci(self, n):
        """
        Calculate the n-th Tribonacci number using an iterative approach.

        The Tribonacci sequence is a generalization of the Fibonacci sequence where each term
        is the sum of the three preceding ones. It starts as:
        T(0) = 0, T(1) = 1, T(2) = 1, T(3) = 2, T(4) = 4, T(5) = 7, T(6) = 13, ...

        Parameters:
            n (int): The index (n >= 0) of the Tribonacci number to compute.

        Returns:
            int: The n-th Tribonacci number.

        Time Complexity:
            O(n) – A single loop from 3 to n.

        Space Complexity:
            O(1) – Constant space used for variables (no recursion or extra memory).
        """

        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Initialize the first three values
        prev = 0      # T(n - 3)
        second = 1    # T(n - 2)
        third = 1     # T(n - 1)
        current = 0   # T(n)

        # Iteratively compute up to n
        for index in range(3, n + 1):
            current = prev + second + third
            prev = second
            second = third
            third = current

        return current


# ------------------------------
# Example usage and test cases
# ------------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: T(4) = 4
    assert solution.tribonacci(4) == 4, "Test Case 1 Failed"

    # Test Case 2: T(6) = 13
    assert solution.tribonacci(6) == 13, "Test Case 2 Failed"

    print("All test cases passed.")
