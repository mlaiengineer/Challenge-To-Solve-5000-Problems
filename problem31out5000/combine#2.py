class Solution(object):
    def combine(self, n, k):
        """
        Generate all possible combinations of k numbers out of the range [1, n].

        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Time Complexity: O(C(n, k)) where C(n, k) = n! / (k!(n-k)!)
            - We generate each valid combination.
            - Each combination takes O(k) time to build (copying the list).

        Space Complexity: O(k) for recursion stack (maximum depth) +
                          O(C(n, k) * k) to store all combinations.
        """

        result = []

        def backtracking(start, current):
            # Base case: when the combination is of length k
            if len(current) == k:
                result.append(current[:])  # append a copy
                return

            # Prune the loop: no need to go beyond (n - (k - len(current)) + 1)
            for j in range(start, n - (k - len(current)) + 2):
                current.append(j)               # Choose
                backtracking(j + 1, current)    # Explore
                current.pop()                  # Un-choose (backtrack)

        backtracking(1, [])
        return result


# ========== TEST CASES ==========
import unittest

class TestCombine(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        # n = 4, k = 2 => Expected 6 combinations
        expected = sorted([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
        result = sorted(self.solution.combine(4, 2))
        self.assertEqual(result, expected)

    def test_case_2(self):
        # n = 1, k = 1 => Only one combination possible
        expected = [[1]]
        result = self.solution.combine(1, 1)
        self.assertEqual(result, expected)

    def test_case_3(self):
        # n = 5, k = 3 => 10 combinations expected
        expected = sorted([
            [1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],
            [2,3,4],[2,3,5],[2,4,5],[3,4,5]
        ])
        result = sorted(self.solution.combine(5, 3))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
