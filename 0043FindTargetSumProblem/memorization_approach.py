class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        Solves the Target Sum problem using a memoized recursive approach.
        This approach is more efficient than the pure recursive solution.
        """
        memo = {}
        
        def backtrack(index, current_sum):
            # If we've processed all numbers...
            if index == len(nums):
                # ...check if the current sum matches the target.
                return 1 if current_sum == target else 0

            # If the current state (index, current_sum) is in our cache...
            if (index, current_sum) in memo:
                # ...return the pre-computed result.
                return memo[(index, current_sum)]
            
            # Explore the two possibilities: adding or subtracting the current number.
            add_path = backtrack(index + 1, current_sum + nums[index])
            subtract_path = backtrack(index + 1, current_sum - nums[index])
            
            # Store the sum of ways from both paths in our cache.
            memo[(index, current_sum)] = add_path + subtract_path
            
            # Return the calculated result for this state.
            return memo[(index, current_sum)]
        
        # Start the recursive process and return the final result.
        return backtrack(0, 0)
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
nums5 = [1,2,3]
target5 = 4
result5 = test_solution.findTargetSumWays(nums3, target3)
print(f"Test Case 5: nums = {nums5}, target = {target5}")
print(f"Expected: 3, Actual: {result5}\n")
