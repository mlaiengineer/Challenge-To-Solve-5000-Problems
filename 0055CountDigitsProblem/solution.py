class Solution:
    def evenlyDivides(self, n):
        """
        Count how many digits of n divide n evenly.

        Args:
            n (int): A positive integer.

        Returns:
            int: Number of digits that divide n without remainder.

        Notes:
            - Digit '0' is ignored to avoid division by zero.
            - Digits are checked individually.
        """

        num_str = str(n)
        count = 0

        for digit in num_str:
            d = int(digit)

            # Skip the digit if it is 0 (cannot divide)
            if d == 0:
                continue

            # Check if the digit divides n evenly
            if n % d == 0:
                count += 1

        return count


# Example test
test_solution = Solution()
print(test_solution.evenlyDivides(23))  # Expected output: 0
