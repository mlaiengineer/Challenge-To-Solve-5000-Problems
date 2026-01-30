class MemoizationSolution(object):
    def minCut(self, s):
        """
        Returns the minimum number of cuts needed to partition the string
        such that every substring is a palindrome.
        """
        n = len(s)

        # palindrome_table[i][j] = True if s[i:j+1] is a palindrome
        palindrome_table = [[False] * n for _ in range(n)]

        # Build palindrome table (Bottom-Up DP)
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                if start == end:
                    palindrome_table[start][end] = True
                elif s[start] == s[end] and (
                    end == start + 1 or palindrome_table[start + 1][end - 1]
                ):
                    palindrome_table[start][end] = True

        # memo[start][end] stores minimum cuts for s[start:end+1]
        memo = [[None] * n for _ in range(n)]

        def min_cuts(start, end):
            """
            Recursively computes minimum cuts needed for s[start:end+1]
            using memoization.
            """

            # Base case: already a palindrome or single character
            if start >= end or palindrome_table[start][end]:
                return 0

            # Return cached result if exists
            if memo[start][end] is not None:
                return memo[start][end]

            # Worst case: cut before every character
            min_cut = end - start

            # Try all possible cut positions
            for cut in range(start, end):
                if palindrome_table[start][cut]:
                    min_cut = min(
                        min_cut,
                        1 + min_cuts(cut + 1, end)
                    )

            memo[start][end] = min_cut
            return min_cut

        return min_cuts(0, n - 1)
