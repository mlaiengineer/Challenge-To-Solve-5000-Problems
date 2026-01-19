class Solution:
    def longest_palindromic_subsequence(self, s: str) -> int:
        """
        Returns the length of the longest palindromic subsequence in string s.

        Dynamic Programming approach:
        dp[i][j] = longest palindromic subsequence length in substring s[i..j]

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        n = len(s)

        # dp[i][j] will store the LPS length of substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Traverse substrings by increasing length (diagonal DP)
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Single character is always palindrome of length 1
                if i == j:
                    dp[i][j] = 1

                # Matching characters on both ends
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]

                # Otherwise take best of removing one side
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
