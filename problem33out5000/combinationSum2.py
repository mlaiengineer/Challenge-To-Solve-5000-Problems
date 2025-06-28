""""
Problem:
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to the target.
Each number in candidates may only be used once in the combination.

Note:
- The solution set must not contain duplicate combinations.

Approach:
- Sort the array to simplify duplicate handling and allow early pruning.
- Use backtracking with a helper function.
- Skip duplicates at the same recursive level to avoid repeated combinations.

Time Complexity:
- O(2^n): Worst-case scenario where all subsets are considered (n = number of candidates).
- Sorting takes O(n log n), and duplicate skipping helps optimize.

Space Complexity:
- O(n): Stack space for recursion and path list (not counting the result list).
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # Sort to simplify duplicate handling
        result = []

        def backtrack(start, path, total):
            # ✅ Found a valid combination
            if total == target:
                result.append(path[:])  # Copy current path
                return

            # 🚫 Exceeded the target sum
            if total > target:
                return

            for i in range(start, len(candidates)):
                # ⚠️ Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # ✅ Choose and move forward
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()  # ❌ Backtrack

        backtrack(0, [], 0)
        return result


# ✅ Test Cases
if __name__ == "__main__":
    solver = Solution()

    print("Test Case 1:")
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print("Input:", candidates1, "| Target:", target1)
    print("Output:", solver.combinationSum2(candidates1, target1))
    print()

    print("Test Case 2:")
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print("Input:", candidates2, "| Target:", target2)
    print("Output:", solver.combinationSum2(candidates2, target2))
    print()

    print("Test Case 3:")
    candidates3 = [3, 1, 3, 5, 1, 1]
    target3 = 8
    print("Input:", candidates3, "| Target:", target3)
    print("Output:", solver.combinationSum2(candidates3, target3))
    print()
