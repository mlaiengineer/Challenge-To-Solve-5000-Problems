class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Finds the length of the longest strictly increasing subsequence (LIS) in the given list.
        
        :param nums: List[int] - The input array of integers.
        :return: int - The length of the longest strictly increasing subsequence.
        """
        n = len(nums)
        # Memoization table initialized with -1
        # dp_table[i][j] stores the LIS length starting from index `i` with the `j`th element as the previous element
        dp_table = [[-1] * (n + 1) for _ in range(n)]
        
        def findLIS(curr_index, prev_index):
            """
            Recursive helper function to compute the LIS using memoization.

            :param curr_index: int - The current index in the array being considered.
            :param prev_index: int - The index of the last included element in the LIS.
            :return: int - The length of the LIS starting from the current index.
            """
            # Base case: If the current index is out of bounds, return 0
            if curr_index >= n:
                return 0

            # Check if the result is already computed
            if dp_table[curr_index][prev_index + 1] != -1:
                return dp_table[curr_index][prev_index + 1]

            # Option 1: Exclude the current element
            exclude = findLIS(curr_index + 1, prev_index)

            # Option 2: Include the current element (if valid)
            include = 0
            if prev_index == -1 or nums[curr_index] > nums[prev_index]:
                include = 1 + findLIS(curr_index + 1, curr_index)

            # Store the result in the memoization table
            dp_table[curr_index][prev_index + 1] = max(exclude, include)

            return dp_table[curr_index][prev_index + 1]

        # Start the recursion with the first element and no previous element
        return findLIS(0, -1)


# Test the solution with multiple test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Array with all elements the same
    nums_1 = [1, 1, 1]
    print(f"Test Case 1: {solution.lengthOfLIS(nums_1)}")  # Expected Output: 1

    # Test Case 2: General case with an increasing subsequence
    nums_2 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Test Case 2: {solution.lengthOfLIS(nums_2)}")  # Expected Output: 4

    # Test Case 3: Strictly increasing array
    nums_3 = [1, 2, 3, 4, 5]
    print(f"Test Case 3: {solution.lengthOfLIS(nums_3)}")  # Expected Output: 5
