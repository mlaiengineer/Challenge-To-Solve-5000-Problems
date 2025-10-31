class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Finds the length of the longest strictly increasing subsequence (LIS) in the given list.
        
        :param nums: List[int] - The input array of integers.
        :return: int - The length of the longest strictly increasing subsequence.
        """
        n = len(nums)

        # Tabulation table initialized with 0
        # dp_table[i][j] represents the LIS length starting from index `i` 
        # with the element at index `j-1` as the previous element in the LIS.
        dp_table = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Iterate over the array from the last index to the first
        for i in range(n - 1, -1, -1):
            # Iterate over the possible previous elements (from `i` to `-1`)
            for j in range(i, -1, -1):
                # Option 1: Exclude the current element and take the LIS length from the next index
                exclude = dp_table[i + 1][j] 

                # Option 2: Include the current element (if valid) and add 1 to the LIS length
                include = 0  # Initialize to 0, as we may not always include the element
                if j - 1 == -1 or nums[i] > nums[j - 1]:
                    include = 1 + dp_table[i + 1][i + 1]

                # Store the maximum of including or excluding the current element
                dp_table[i][j] = max(exclude, include)

        # The answer is stored in dp_table[0][0], 
        # which represents the LIS length starting from index 0 with no previous element
        return dp_table[0][0]
            

# Test the solution with multiple test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Strictly decreasing array
    nums_1 = [5, 4, 3, 2, 1]
    print(f"Test Case 1: {solution.lengthOfLIS(nums_1)}")  # Expected Output: 1

    # Test Case 2: Mixed positive and negative numbers
    nums_2 = [-1, 3, 4, -2, 0, 6, 2, 3]
    print(f"Test Case 2: {solution.lengthOfLIS(nums_2)}")  # Expected Output: 4

    # Test Case 3: Single element array
    nums_3 = [10]
    print(f"Test Case 3: {solution.lengthOfLIS(nums_3)}")  # Expected Output: 1
