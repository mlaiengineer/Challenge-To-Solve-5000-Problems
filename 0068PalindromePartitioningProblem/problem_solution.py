from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Returns all possible palindrome partitioning of the string s.

        Approach:
        1. Precompute a DP table where is_palindrome[i][j] indicates
           whether s[i:j+1] is a palindrome.
        2. Use backtracking to generate all valid partitions using the DP table.

        Time Complexity: O(n * 2^n)
        Space Complexity: O(n^2)
        """
        n = len(s)

        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        # Fill the DP table diagonally
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if i == j:
                    is_palindrome[i][j] = True
                elif s[i] == s[j] and (j == i + 1 or is_palindrome[i + 1][j - 1]):
                    is_palindrome[i][j] = True

        result: List[List[str]] = []

        def backtrack(start: int, current_partition: List[str]) -> None:
            # Base case: reached the end of the string
            if start == n:
                result.append(current_partition[:])
                return

            # Try all possible end positions
            for end in range(start, n):
                if is_palindrome[start][end]:
                    current_partition.append(s[start:end + 1])
                    backtrack(end + 1, current_partition)
                    current_partition.pop()  # backtracking step

        backtrack(0, [])
        return result
