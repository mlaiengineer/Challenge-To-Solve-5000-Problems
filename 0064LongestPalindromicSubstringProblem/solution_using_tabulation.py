class Solution(object):
    def longestPalindrome(self, s):
        """
        Find the longest palindromic substring using
        bottom-up dynamic programming.

        :type s: str
        :rtype: str
        """
        n = len(s)

        # dp[i][j] = True if substring s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]

        # At least the first character is a palindrome
        longest = s[0]

        # Iterate over all possible substring lengths
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Case 1: Single character
                if i == j:
                    dp[i][j] = True

                # Case 2: Two characters or more
                elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False

                # Update longest palindrome found
                if dp[i][j] and length > len(longest):
                    longest = s[i:j + 1]

        return longest
