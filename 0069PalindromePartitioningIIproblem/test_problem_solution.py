from recursion_solution import Solution


def test_min_cut():
    solution = Solution()

    # Basic cases
    assert solution.minCut("a") == 0
    assert solution.minCut("ab") == 1
    assert solution.minCut("aa") == 0

    # Given examples
    assert solution.minCut("aab") == 1

    # More cases
    assert solution.minCut("aabb") == 1        # "aa" | "bb"
    assert solution.minCut("ababbbabbababa") == 3
    assert solution.minCut("racecar") == 0
    assert solution.minCut("banana") == 1      # "b" | "anana"
    assert solution.minCut("cdd") == 1          # "c" | "dd"
    assert solution.minCut("noonabbad") == 2    # "noon" | "abba" | "d"

    print("✅ All 10 test cases passed!")


if __name__ == "__main__":
    test_min_cut()
