from problem_solution import Solution


def test_longest_palindromic_subsequence():
    solution = Solution()

    # Basic cases
    assert solution.longest_palindromic_subsequence("a") == 1
    assert solution.longest_palindromic_subsequence("aa") == 2

    # Examples from LeetCode
    assert solution.longest_palindromic_subsequence("bbbab") == 4
    assert solution.longest_palindromic_subsequence("cbbd") == 2

    # Edge / diverse cases
    assert solution.longest_palindromic_subsequence("abcde") == 1
    assert solution.longest_palindromic_subsequence("aaa") == 3
    assert solution.longest_palindromic_subsequence("agbdba") == 5

    print("✅ All test cases passed!")


if __name__ == "__main__":
    test_longest_palindromic_subsequence()
