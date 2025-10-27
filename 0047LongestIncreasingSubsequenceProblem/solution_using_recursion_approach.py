class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Finds the length of the longest strictly increasing subsequence (LIS) in the given list.
        
        :param nums: List[int] - The input array of integers.
        :return: int - The length of the longest strictly increasing subsequence.
        """
        n = len(nums)

        # Helper function to recursively find the LIS
        def helper(curr_index, prev_index):
            """
            Recursive helper function to compute the LIS.

            :param curr_index: int - The current index in the array being considered.
            :param prev_index: int - The index of the previously included element in the LIS.
            :return: int - The length of the LIS from the current index.
            """
            # Base case: If the current index exceeds the array length, return 0
            if curr_index >= n:
                return 0

            # Option 1: Exclude the current element from the LIS
            exclude = helper(curr_index + 1, prev_index)

            # Option 2: Include the current element in the LIS (if valid)
            include = 0
            # The validity check: either no previous element, or the current element is greater
            if prev_index == -1 or nums[curr_index] > nums[prev_index]:
                include = 1 + helper(curr_index + 1, curr_index)

            # Return the maximum of including or excluding the current element
            return max(exclude, include)

        # Start the recursion with the first element and no previous element
        return helper(0, -1)


# Test the solution with multiple test cases
if __name__ == "__main__":
    test_solution = Solution()

    # Test Case 1: Simple case with constant values
    nums_1 = [1, 1, 1]
    print(f"Test Case 1: {test_solution.lengthOfLIS(nums_1)}")  # Expected Output: 1

    # Test Case 2: General case with an increasing subsequence
    nums_2 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Test Case 2: {test_solution.lengthOfLIS(nums_2)}")  # Expected Output: 4

    # Test Case 3: Strictly increasing array
    nums_3 = [1, 2, 3, 4, 5]
    print(f"Test Case 3: {test_solution.lengthOfLIS(nums_3)}")  # Expected Output: 5
