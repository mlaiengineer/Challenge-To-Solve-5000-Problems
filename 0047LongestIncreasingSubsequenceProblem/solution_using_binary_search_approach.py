class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Find the length of the Longest Increasing Subsequence (LIS).

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            int: Length of the longest strictly increasing subsequence.
        """

        # Binary search helper function
        def binary_search(sub, num):
            """
            Find the index where 'num' should be placed in 'sub'
            to maintain increasing order.
            """
            left, right = 0, len(sub) - 1

            while left < right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left

        # 'sub' will store the smallest possible tail of all increasing
        # subsequences of different lengths
        sub = [nums[0]]

        for num in nums[1:]:
            # If current number extends the LIS
            if num > sub[-1]:
                sub.append(num)
            else:
                # Replace the first number >= num using binary search
                index = binary_search(sub, num)
                sub[index] = num

        # Length of 'sub' equals length of LIS
        return len(sub)


# Test cases
test_solution = Solution()

print(test_solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(test_solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))           # 4
print(test_solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))        # 1
