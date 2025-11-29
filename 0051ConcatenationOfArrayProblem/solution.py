class Solution(object):
    def getConcatenation(self, nums):
        """
        Calculates the concatenation of an array with itself (ans = nums + nums).

        The resulting array 'ans' has a length of 2n, where ans[i] == nums[i]
        and ans[i + n] == nums[i] for 0 <= i < n.

        :type nums: List[int]  # The input integer array.
        :rtype: List[int]      # The concatenated array of length 2n.
        """
        n = len(nums)
        # 1. Initialize the result array 'ans' with a length of 2n
        ans = [0] * (n * 2)

        # 2. Iterate through the entire 'ans' array (from index 0 to 2n - 1)
        for i in range(len(ans)):
            # 3. Core logic: Use the modulo operator (i % n) to map the index
            #    of the target array 'ans' back to the correct index in 'nums'.
            #    - For i < n, i % n is i (First copy of nums)
            #    - For i >= n, i % n is i - n (Second copy of nums)
            ans[i] = nums[i % n]

        return ans

# --- Example Usage (Keep separate from the class definition for clarity) ---
test_solution = Solution()
print(test_solution.getConcatenation([1, 2, 1]))    # Output: [1, 2, 1, 1, 2, 1]
print(test_solution.getConcatenation([1, 3, 2, 1])) # Output: [1, 3, 2, 1, 1, 3, 2, 1]