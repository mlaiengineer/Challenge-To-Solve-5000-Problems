from problem_solution import Solution


def test_palindrome_partitioning():
    solution = Solution()

    # Helper to compare results ignoring order
    def normalize(result):
        return sorted(result)

    # Test case 1 (LeetCode example)
    assert normalize(solution.partition("aab")) == normalize(
        [["a", "a", "b"], ["aa", "b"]]
    )

    # Test case 2 (single character)
    assert normalize(solution.partition("a")) == normalize([["a"]])

    # Test case 3 (all same characters)
    assert normalize(solution.partition("aaa")) == normalize(
        [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    )

    # Test case 4 (no multi-character palindrome)
    assert normalize(solution.partition("abc")) == normalize(
        [["a", "b", "c"]]
    )

    print("✅ Passed all test cases!")


if __name__ == "__main__":
    test_palindrome_partitioning()
