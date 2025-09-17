class Solution(object):
    def canPartition(self, nums):
        """
        Determines if the given array can be partitioned into two subsets 
        with equal sums.

        Args:
        nums (List[int]): The list of integers.

        Returns:
        bool: True if the array can be partitioned into two subsets with equal sums, False otherwise.
        """
        # Calculate the total sum of all elements in the array
        total_sum = sum(nums)
        
        # If the total sum is odd, it's impossible to split the array into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        # Target is half of the total sum (what each subset should sum to)
        target_sum = total_sum // 2
        
        # Use a set to track possible subset sums
        possible_sums = {0}
        
        # Iterate through each number in the array
        for number in nums:
            # Create a temporary set to store new sums for this iteration
            new_sums = set()
            
            # Check all existing sums in the possible_sums set
            for current_sum in possible_sums:
                # Add the current number to the existing sum to form a new sum
                new_sum = current_sum + number
                new_sums.add(new_sum)
            
            # Update the possible_sums set with the new sums
            possible_sums.update(new_sums)
        
        # If the target sum exists in the possible sums, return True
        if target_sum in possible_sums:
            return True
        
        # Otherwise, return False
        return False


# Test cases
test_solution = Solution()

# Test Case 1: Evenly divisible into two subsets
nums1 = [1, 5, 11, 5]
# Explanation: Can be partitioned into [1, 5, 5] and [11], both summing to 11.
print(test_solution.canPartition(nums1))  # Expected output: True

# Test Case 2: Cannot be partitioned
nums2 = [1, 2, 3, 5]
# Explanation: Cannot be partitioned into two subsets with equal sums.
print(test_solution.canPartition(nums2))  # Expected output: False

# Test Case 3: Single element (edge case)
nums3 = [7]
# Explanation: A single element cannot be divided into two subsets.
print(test_solution.canPartition(nums3))  # Expected output: False
