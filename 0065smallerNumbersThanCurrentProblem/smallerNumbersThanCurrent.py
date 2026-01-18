class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        For each element in the array, count how many numbers
        are strictly smaller than it.

        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        # Iterate over each number
        for i in range(len(nums)):
            current_value = nums[i]
            smaller_count = 0

            # Compare with all other numbers
            for j in range(len(nums)):
                if nums[j] < current_value:
                    smaller_count += 1

            result.append(smaller_count)

        return result
