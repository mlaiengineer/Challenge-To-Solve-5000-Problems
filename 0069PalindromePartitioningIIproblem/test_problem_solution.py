from recursion_solution import RecursionSolution
from memoization_solution import MemoizationSolution


TEST_CASES = [
    ("a", 0),
    ("ab", 1),
    ("aa", 0),
    ("aab", 1),
    ("aabb", 1),
    ("ababbbabbababa", 3),
    ("racecar", 0),
    ("banana", 1),
    ("cdd", 1),
    ("noonabbad", 2),
]


def test_recursion_solution():
    solution = RecursionSolution()
    for string, expected in TEST_CASES:
        assert solution.minCut(string) == expected
    print("✅ Recursion solution passed all tests")


def test_memoization_solution():
    solution = MemoizationSolution()
    for string, expected in TEST_CASES:
        assert solution.minCut(string) == expected
    print("✅ Memoization solution passed all tests")


if __name__ == "__main__":
    test_recursion_solution()
    test_memoization_solution()
