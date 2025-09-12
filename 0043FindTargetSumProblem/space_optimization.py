class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        Solves the Target Sum problem using dynamic programming with space optimization.
        We use hash maps (dictionaries) to store the number of ways to reach each possible sum
        after processing each number.
        """

        # dp_map keeps track of {sum_value: number_of_ways_to_get_this_sum}
        dp_map = {}

        # Handle the first number separately
        if nums[0] == 0:
            # If the first number is 0, we can assign both +0 and -0,
            # which both result in 0 but count as two distinct ways
            dp_map[0] = 2
        else:
            # Otherwise, we can either add or subtract the first number
            dp_map[nums[0]] = 1
            dp_map[-nums[0]] = 1

        # Process the rest of the numbers
        for i in range(1, len(nums)):
            next_map = {}  # Temporary map for the current step
            current_num = nums[i]

            # For each sum we've reached so far
            for prev_sum, count in dp_map.items():
                # Option 1: Add the current number
                new_sum_add = prev_sum + current_num
                next_map[new_sum_add] = next_map.get(new_sum_add, 0) + count

                # Option 2: Subtract the current number
                new_sum_sub = prev_sum - current_num
                next_map[new_sum_sub] = next_map.get(new_sum_sub, 0) + count

            # Move to the next step
            dp_map = next_map

        # Return the number of ways to reach the target sum (0 if none)
        return dp_map.get(target, 0)
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
