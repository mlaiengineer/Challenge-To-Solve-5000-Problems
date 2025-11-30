class Solution(object):
    def shuffle(self, nums, n):
        """
        Rearranges an array in the format:
        [x1, x2, ..., xn, y1, y2, ..., yn]
        into:
        [x1, y1, x2, y2, ..., xn, yn]

        Args:
            nums (List[int]): Input array of length 2n.
            n (int): Half the length of nums.

        Returns:
            List[int]: The shuffled array.
        """

        # Split nums into the X-part and Y-part
        x = nums[:n]      # First n elements: x1, x2, ..., xn
        y = nums[n:]      # Last n elements: y1, y2, ..., yn

        # Prepare result array with exact size (2n)
        shuffle_nums = [0] * (2 * n)

        # Fill even indices (0, 2, 4...) with x-values
        shuffle_nums[0::2] = x

        # Fill odd indices (1, 3, 5...) with y-values
        shuffle_nums[1::2] = y

        return shuffle_nums


# Example usage:
nums = [2, 5, 1, 3, 4, 7]
n = 3

test_solution = Solution()
print(test_solution.shuffle(nums, n))  # Expected output: [2, 3, 5, 4, 1, 7]
