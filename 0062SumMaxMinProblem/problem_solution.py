class Solution:
    def findSum(self, A, N):
        """
        Finds the sum of the minimum and maximum elements in an array.

        :param A: List[int] - array of integers
        :param N: int - size of the array
        :return: int - sum of min and max elements
        """

        # Edge case: empty array
        if N == 0:
            return 0

        # Initialize min and max with the first element
        min_num = A[0]
        max_num = A[0]

        # Traverse the array to find min and max
        for i in range(1, N):
            if A[i] > max_num:
                max_num = A[i]
            if A[i] < min_num:
                min_num = A[i]

        # Return the sum of min and max
        return min_num + max_num

def test_find_sum():
    solution = Solution()

    # Test case 1: Normal case
    assert solution.findSum([1, 3, 4, 1], 4) == 5

    # Test case 2: Single element
    assert solution.findSum([10], 1) == 20

    # Test case 3: Negative numbers
    assert solution.findSum([-5, -1, -9, -3], 4) == -10

    # Test case 4: Mixed positive and negative
    assert solution.findSum([-2, 0, 5, 3], 4) == 3

    # Test case 5: Empty array
    assert solution.findSum([], 0) == 0

    print("All test cases passed!")
