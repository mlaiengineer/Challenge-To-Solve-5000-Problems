class Solution(object):
    def countSubstrings(self, s):
        n = len(s)

        # dp[i][j] = True if substring s[i:j] is palindrome
        dp = [[False] * n for _ in range(n)]

        result = 0

        # l = length of substring
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if i == j:
                    dp[i][j] = True

                elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                if dp[i][j]:
                    result += 1

        return result


# 🧪 Test Cases

def test_countSubstrings():
    solution = Solution()

    # Basic tests
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6

    # Additional tests
    assert solution.countSubstrings("aba") == 4
    assert solution.countSubstrings("abba") == 6
    assert solution.countSubstrings("a") == 1

    print("All test cases passed ✅")

if __name__ == "__main__":
    test_countSubstrings()