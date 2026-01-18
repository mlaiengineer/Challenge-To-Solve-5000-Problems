from smallerNumbersThanCurrent import Solution
from solution import Solution


def test_smallerNumbersThanCurrent():
    solution = Solution()

    # Example tests from problem
    assert solution.smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]
    assert solution.smallerNumbersThanCurrent([6,5,4,8]) == [2,1,0,3]
    assert solution.smallerNumbersThanCurrent([7,7,7,7]) == [0,0,0,0]

    # Edge cases
    assert solution.smallerNumbersThanCurrent([1,2]) == [0,1]
    assert solution.smallerNumbersThanCurrent([5]) == [0]

    print("All test cases passed ✅")


if __name__ == "__main__":
    test_smallerNumbersThanCurrent()
