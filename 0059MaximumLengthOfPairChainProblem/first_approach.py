class Solution(object):
    def findLongestChain(self, pairs):
        """
        Finds the longest chain of pairs.

        A pair (a, b) can be followed by (c, d) if b < c.

        :type pairs: List[List[int]]
        :rtype: int
        """

        # Edge case: no pairs
        if not pairs:
            return 0

        # Step 1: Sort pairs based on their first value
        pairs.sort()

        n = len(pairs)

        # Step 2: Initialize DP table
        # dp[i] represents the longest chain ending at index i
        dp = [1] * n

        longest_chain = 1

        # Step 3: Build the DP table
        for i in range(1, n):
            for j in range(i):
                # Check if current pair can extend the previous chain
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

            # Update global maximum
            longest_chain = max(longest_chain, dp[i])

        return longest_chain


# =====================
# Test Cases
# =====================

solution = Solution()

# Test Case 1: Simple chain
pairs1 = [[1, 2], [3, 4], [5, 6]]
print(solution.findLongestChain(pairs1))  # Expected: 3

# Test Case 2: Overlapping pairs
pairs2 = [[1, 2], [2, 3], [3, 4]]
print(solution.findLongestChain(pairs2))  # Expected: 2

# Test Case 3: Unordered input
pairs3 = [[5, 6], [1, 2], [3, 4]]
print(solution.findLongestChain(pairs3))  # Expected: 3

# Test Case 4: Single pair
pairs4 = [[1, 10]]
print(solution.findLongestChain(pairs4))  # Expected: 1

# Test Case 5: Empty input
pairs5 = []
print(solution.findLongestChain(pairs5))  # Expected: 0
