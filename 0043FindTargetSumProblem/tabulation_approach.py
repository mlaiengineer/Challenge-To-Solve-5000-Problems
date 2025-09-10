class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        Solves the Target Sum problem using a tabulation approach.
        This approach is more efficient than the pure recursive solution.
        """
        dp_table = {}

        # Base case: Initialize the table with the first number's possibilities.
        if nums[0] == 0:
            dp_table[0] = 2
        else:
            dp_table[nums[0]] = 1
            dp_table[-nums[0]] = 1

        # Iterate through the rest of the numbers to build the DP table.
        for i in range(1, len(nums)):
            next_dp_table = {} 
            current_num = nums[i]
            
            for prev_sum, count in dp_table.items():
                # For each previous sum, calculate the new sums by adding and subtracting
                
                # 1. Add the current number
                new_add_sum = prev_sum + current_num
                next_dp_table[new_add_sum] = next_dp_table.get(new_add_sum, 0) + count

                # 2. Subtract the current number
                new_sub_sum = prev_sum - current_num
                next_dp_table[new_sub_sum] = next_dp_table.get(new_sub_sum, 0) + count
            
            # Update the main DP table for the next iteration
            dp_table = next_dp_table
        
        # After processing all numbers, return the count for the target sum.
        # Use .get() to return 0 if the target is not a key in the final table.
        return dp_table.get(target, 0)

# --- Test Cases ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Simple, multiple solutions
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    result1 = solution.findTargetSumWays(nums1, target1)
    print(f"Test Case 1:")
    print(f"  Input: nums={nums1}, target={target1}")
    print(f"  Expected Output: 5")
    print(f"  Actual Output: {result1}")
    print("-" * 20)

    # Test Case 2: A simple case
    nums2 = [1]
    target2 = 1
    result2 = solution.findTargetSumWays(nums2, target2)
    print(f"Test Case 2:")
    print(f"  Input: nums={nums2}, target={target2}")
    print(f"  Expected Output: 1")
    print(f"  Actual Output: {result2}")
    print("-" * 20)

    # Test Case 3: A case with a zero in the input
    nums3 = [1, 0, 1]
    target3 = 2
    result3 = solution.findTargetSumWays(nums3, target3)
    print(f"Test Case 3:")
    print(f"  Input: nums={nums3}, target={target3}")
    print(f"  Expected Output: 2")
    print(f"  Actual Output: {result3}")
    print("-" * 20)

    # Test Case 4: No solution exists
    nums4 = [1, 2, 3]
    target4 = 10
    result4 = solution.findTargetSumWays(nums4, target4)
    print(f"Test Case 4:")
    print(f"  Input: nums={nums4}, target={target4}")
    print(f"  Expected Output: 0")
    print(f"  Actual Output: {result4}")
    print("-" * 20)
