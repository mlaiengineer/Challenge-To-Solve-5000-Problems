from solution_using_tabulation import Solution
def test_longestPalindrome():
    solution = Solution()

    # Basic tests
    assert solution.longestPalindrome("babad") in ["bab", "aba"]
    assert solution.longestPalindrome("cbbd") == "bb"

    # Edge cases
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("aaaa") == "aaaa"

    # Mixed cases
    assert solution.longestPalindrome("racecar") == "racecar"
    assert solution.longestPalindrome("abacdfgdcaba") == "aba"

    print("All test cases passed ✅")


if __name__ == "__main__":
    test_longestPalindrome()
