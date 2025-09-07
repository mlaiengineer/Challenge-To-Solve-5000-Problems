class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        Finds the number of ways to assign plus and minus signs to
        the numbers in `nums` to achieve the `target` sum.

        This solution uses a recursive approach with backtracking to
        explore all possible combinations.

        :param nums: A list of integers.
        :param target: The target sum to achieve.
        :return: The number of ways to achieve the target sum.
        """
        
        # A variable to keep track of the total number of valid ways.
        self.count = 0

        def backtrack(index, current_sum):
            """
            The recursive helper function to explore all possibilities.

            :param index: The current index in the nums array.
            :param current_sum: The sum of numbers processed so far.
            """
            
            # Base Case: If we have processed all the numbers in the array.
            if index == len(nums):
                # If the current sum equals the target, we've found a valid way.
                if current_sum == target:
                    self.count += 1
                return

            # Recursive Step: Explore both possibilities (+ and -).

            # 1. Add the current number and proceed to the next index.
            backtrack(index + 1, current_sum + nums[index])

            # 2. Subtract the current number and proceed to the next index.
            backtrack(index + 1, current_sum - nums[index])

        # Start the backtracking process from the beginning of the array with a sum of 0.
        backtrack(0, 0)
        return self.count

# Create an instance of the Solution class
test_solution = Solution()

# Test Case 1: Simple case from LeetCode problem description
nums1 = [1, 1, 1, 1, 1]
target1 = 3
result1 = test_solution.findTargetSumWays(nums1, target1)
print(f"Test Case 1: nums = {nums1}, target = {target1}")
print(f"Expected: 5, Actual: {result1}\n")

# Test Case 2: Another simple case
nums2 = [2, 1]
target2 = 1
result2 = test_solution.findTargetSumWays(nums2, target2)
print(f"Test Case 2: nums = {nums2}, target = {target2}")
print(f"Expected: 1, Actual: {result2}\n")

# Test Case 3: Case with a negative target
nums3 = [5, 4, 3, 2, 1]
target3 = -1
result3 = test_solution.findTargetSumWays(nums3, target3)
print(f"Test Case 3: nums = {nums3}, target = {target3}")
print(f"Expected: 2, Actual: {result3}\n")

# Test Case 4: Case with zeros, which adds more complexity
# Note: +0 and -0 are the same, but the recursive path still doubles.
# This test shows how the algorithm handles this.
nums4 = [0, 0, 1]
target4 = 1
result4 = test_solution.findTargetSumWays(nums4, target4)
print(f"Test Case 4: nums = {nums4}, target = {target4}")
print(f"Expected: 4, Actual: {result4}\n") 
# Explanation: [1,0,0], [1,0,0], [1,0,0], [1,0,0] all evaluate to 1.
# This is because the two zeros can be either +0 or -0, leading to
# 2 * 2 = 4 combinations that result in the same sum.
