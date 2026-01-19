from problem_solution import Solution

def test_longestPalindromicSubsequence():
    solution = Solution()

    assert solution.longestPalindromeSubseq("abd") == 1

    assert solution.longestPalindromeSubseq("bbbab") == 4
    print("Passed All test Cases")



if __name__ == "__main__":
    test_longestPalindromicSubsequence()