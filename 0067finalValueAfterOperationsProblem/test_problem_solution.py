from problem_solution import Solution


def test_final_value_after_operations():
    solution = Solution()

    # Examples from LeetCode
    assert solution.final_value_after_operations(["--X", "X++", "X++"]) == 1
    assert solution.final_value_after_operations(["++X", "++X", "X++"]) == 3
    assert solution.final_value_after_operations(["X++", "++X", "--X", "X--"]) == 0

    # Additional cases
    assert solution.final_value_after_operations(["++X"]) == 1
    assert solution.final_value_after_operations(["--X"]) == -1
    assert solution.final_value_after_operations([]) == 0

    print("✅ All test cases passed!")


if __name__ == "__main__":
    test_final_value_after_operations()
