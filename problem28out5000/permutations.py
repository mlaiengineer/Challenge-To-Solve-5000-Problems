class Solution(object):
    def permute(self, nums):
        """
        Generates all possible permutations of a list of integers.

        :type nums: List[int]
        :rtype: List[List[int]]

        Time Complexity: O(n * n!)
            - There are n! permutations for a list of size n.
            - Each permutation requires O(n) time to copy the list.

        Space Complexity: O(n)
            - The recursion call stack can go up to depth n.
            - The output list result is not counted in auxiliary space.
        """
        result = []
        def backtrack(index):
            # Base case: if index reaches the end, store the current permutation
            if index == len(nums):
                result.append(nums[:])  # Append a copy of the current permutation
                return

            for j in range(index, len(nums)):
                # Swap the current index with the jth element
                nums[index], nums[j] = nums[j], nums[index]

                # Recurse on the next index
                backtrack(index + 1)

                # Backtrack: revert the swap
                nums[index], nums[j] = nums[j], nums[index]


        backtrack(0)
        return result


# --------------------------
# ✅ Test Cases
# --------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Normal case
    print("Permutations of [1, 2, 3]:")
    print(solution.permute([1, 2, 3]))

    # Test case 2: Two elements
    print("\nPermutations of [0, 1]:")
    print(solution.permute([0, 1]))

    # Test case 3: Single element
    print("\nPermutations of [5]:")
    print(solution.permute([5]))
