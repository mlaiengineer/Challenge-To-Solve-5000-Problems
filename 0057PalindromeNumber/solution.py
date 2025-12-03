class Solution(object):
    def isPalindrome(self, x):
        """
        Check whether an integer is a palindrome by converting it to a string.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if x reads the same forward and backward, False otherwise.
        """

        convert_x_to_str = str(x)      # Convert the number to a string
        reverse_x = ""                 # Will store the reversed version

        # Build the reversed string manually
        for digit in convert_x_to_str:
            reverse_x = digit + reverse_x

        # A palindrome reads the same forward and backward
        return convert_x_to_str == reverse_x


# Quick tests
test_solution = Solution()
print(test_solution.isPalindrome(121))   # True
print(test_solution.isPalindrome(-121))  # False
print(test_solution.isPalindrome(10))    # False
