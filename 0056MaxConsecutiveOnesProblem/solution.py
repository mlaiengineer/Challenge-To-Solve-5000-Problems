class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Find the maximum number of consecutive 1's in a binary array.

        Args:
            nums (List[int]): Binary array containing only 0s and 1s.

        Returns:
            int: Length of the longest consecutive sequence of 1s.
        """

        current_count = 0   # Tracks the current streak of consecutive 1s
        max_ones = 0        # Stores the longest streak found so far

        for value in nums:
            if value == 1:
                current_count += 1              # Extend current streak
                max_ones = max(max_ones, current_count)  # Update maximum if needed
            else:
                current_count = 0               # Reset streak when a 0 appears

        return max_ones


# Example test
test_solution = Solution()
nums = [1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
print(test_solution.findMaxConsecutiveOnes(nums))  # Expected output: 3
