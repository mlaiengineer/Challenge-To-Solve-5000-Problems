"""
LeetCode Problem: Subsets II (https://leetcode.com/problems/subsets-ii/)

Given an integer array `nums` that may contain duplicates, return all possible 
subsets (the power set) without duplicate subsets. The solution set must not 
contain duplicate subsets, and you may return the solution in any order.

Time Complexity: O(2^n)
- Each element has two choices: include or exclude.
- In the worst case (no duplicates), we generate all 2^n subsets.
- Skipping duplicates improves practical performance.

Space Complexity: O(n)
- The depth of the recursion stack is at most n.
- The `path` list uses up to O(n) space in each call.
- The final result list will contain up to 2^n subsets.
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the input array to handle duplicates
        result = []

        def backtrack(start, path):
            """
            Recursively generate subsets using backtracking.

            :param start: Current index to start from
            :param path: The current subset being built
            """
            result.append(path[:])  # Add a copy of the current subset

            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])          # Choose nums[i]
                backtrack(i + 1, path)        # Recurse with next index
                path.pop()                    # Backtrack to explore other options

        backtrack(0, [])
        return result


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
def run_tests():
    sol = Solution()

    test_cases = [
        {
            "input": [1, 2, 2],
            "expected": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        },
        {
            "input": [0],
            "expected": [[], [0]]
        },
        {
            "input": [4, 4, 4, 1, 4],
            "expected": [
                [], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4],
                [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]
            ]
        }
    ]

    for i, case in enumerate(test_cases, 1):
        input_data = case["input"]
        expected_output = sorted([sorted(x) for x in case["expected"]])
        actual_output = sorted([sorted(x) for x in sol.subsetsWithDup(input_data)])
        success = actual_output == expected_output

        print(f"Test Case {i}: {'✅ Passed' if success else '❌ Failed'}")
        if not success:
            print("  Input:    ", input_data)
            print("  Expected: ", case["expected"])
            print("  Got:      ", sol.subsetsWithDup(input_data))
        print()

if __name__ == "__main__":
    run_tests()
