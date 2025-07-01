class Solution(object):
    def combinationSum3(self, k, n):
        """
        Find all possible combinations of k numbers that add up to n,
        using numbers 1 through 9 with each number used at most once.

        :type k: int - number of elements in each combination
        :type n: int - target sum
        :rtype: List[List[int]] - list of valid combinations

        Time Complexity: O(C(9, k)) — Worst-case, all combinations of k out of 9 numbers are explored.
        Space Complexity: O(k) — Stack space used by recursion and O(C(9,k)) for result storage.
        """
        results = []

        def backtracking(k_remaining, target_sum, start_num, current_combination):
            # ✅ Base case: valid combination found
            if k_remaining == 0 and target_sum == 0:
                results.append(current_combination[:])  # Append a copy
                return
            # ❌ Invalid path: either too many numbers or sum exceeded
            if k_remaining < 0 or target_sum < 0:
                return
            # 🔁 Try all numbers from start_num to 9
            for number in range(start_num, 10):
                current_combination.append(number)  # Choose
                # Recursively explore with updated values
                backtracking(k_remaining - 1, target_sum - number, number + 1, current_combination)
                current_combination.pop()  # Backtrack

        # Start the backtracking process
        backtracking(k, n, 1, [])
        return results


# ✅ Test Cases to validate the implementation
if __name__ == "__main__":
    solver = Solution()

    print("✅ Test Case 1:")
    k, n = 3, 7
    print("Input:", k, "| Target:", n)
    print("Output:", solver.combinationSum3(k, n))  # Expected: [[1,2,4]]

    print("\n✅ Test Case 2:")
    k, n = 3, 9
    print("Input:", k, "| Target:", n)
    print("Output:", solver.combinationSum3(k, n))  # Expected: [[1,2,6],[1,3,5],[2,3,4]]

    print("\n✅ Test Case 3:")
    k, n = 4, 1
    print("Input:", k, "| Target:", n)
    print("Output:", solver.combinationSum3(k, n))  # Expected: []

    print("\n✅ Test Case 4:")
    k, n = 2, 17
    print("Input:", k, "| Target:", n)
    print("Output:", solver.combinationSum3(k, n))  # Expected: [[8,9]]
