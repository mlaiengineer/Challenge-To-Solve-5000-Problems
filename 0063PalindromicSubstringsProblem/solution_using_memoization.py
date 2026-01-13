class Solution(object):
    def countSubstrings(self, s):
        """
        Count the number of palindromic substrings using
        recursion + memoization (top-down DP).

        :type s: str
        :rtype: int
        """
        n = len(s)

        # memo[i][j] = True if s[i:j+1] is palindrome, False otherwise
        memo = [[None] * n for _ in range(n)]

        def is_palindrome(left, right):
            """
            Returns True if s[left:right+1] is a palindrome.
            Uses memoization to avoid recomputation.
            """
            # Base cases
            if left >= right:
                return True

            if memo[left][right] is not None:
                return memo[left][right]

            # Recursive check
            memo[left][right] = (
                s[left] == s[right] and is_palindrome(left + 1, right - 1)
            )
            return memo[left][right]

        count = 0

        # Check all possible substrings
        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    count += 1

        return count

def test_countSubstrings():
    solution = Solution()

    # Basic cases
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6

    # Edge cases
    assert solution.countSubstrings("a") == 1
    assert solution.countSubstrings("abba") == 6  # a, b, b, a, bb, abba

    # Mixed cases
    assert solution.countSubstrings("aba") == 4

    print("All test cases passed ✅")


if __name__ == "__main__":
    test_countSubstrings()
