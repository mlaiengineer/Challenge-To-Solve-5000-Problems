class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        Russian Doll Envelopes
        Optimized solution using Longest Increasing Subsequence (LIS)
        with Binary Search.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        if not envelopes:
            return 0

        # Step 1: Sort envelopes
        # Width ascending, height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: LIS on heights using binary search
        lis = []

        for _, height in envelopes:
            left, right = 0, len(lis)

            # Binary search to find position of height
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < height:
                    left = mid + 1
                else:
                    right = mid

            # Replace or append
            if left < len(lis):
                lis[left] = height
            else:
                lis.append(height)

        return len(lis)
def test_max_envelopes():
    solution = Solution()

    # Test case 1: Example from problem
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    assert solution.maxEnvelopes(envelopes) == 3

    # Test case 2: Single envelope
    envelopes = [[1,1]]
    assert solution.maxEnvelopes(envelopes) == 1

    # Test case 3: No envelopes
    envelopes = []
    assert solution.maxEnvelopes(envelopes) == 0

    # Test case 4: Same width, different heights
    envelopes = [[2,3],[2,2],[2,4]]
    assert solution.maxEnvelopes(envelopes) == 1

    # Test case 5: Already sorted increasing
    envelopes = [[1,1],[2,2],[3,3],[4,4]]
    assert solution.maxEnvelopes(envelopes) == 4

    print("All test cases passed!")
