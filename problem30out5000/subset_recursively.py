class Solution(object):
    def subsets(self, nums):
        """
        Generate all subsets (the power set) of a list of unique integers.
        
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Time Complexity: O(2^n) - Each element has 2 choices (include or not).
        Space Complexity: O(2^n) for the result + O(n) for recursion stack.
        """
        result = []

        def backtrack(index, subset):
            # Base case: if we've processed all elements
            if index == len(nums):
                result.append(subset[:])  # Add a copy of the current subset
                return

            # Exclude the current element
            backtrack(index + 1, subset)

            # Include the current element
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Backtrack: remove the last element before the next choice
            subset.pop()

        backtrack(0, [])
        return result

# 🔍 Test Cases
sol = Solution()

print("Test Case 1: [1, 2, 3]")
print(sol.subsets([1, 2, 3]))
# Expected output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

print("\nTest Case 2: [0]")
print(sol.subsets([0]))
# Expected output: [[], [0]]

print("\nTest Case 3: [5, 10]")
print(sol.subsets([5, 10]))
# Expected output: [[], [5], [10], [5, 10]]
