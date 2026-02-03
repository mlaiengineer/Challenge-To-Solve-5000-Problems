class TabulationSolution(object):
    def minCut(self, s):
        """
        Returns the minimum number of cuts needed to partition the string
        such that every substring is a palindrome.
        """
        n = len(s)

        # palindrome_table[i][j] = True if s[i:j+1] is a palindrome
        palindrome_table = [[False] * n for _ in range(n)]
        cuts = [float('inf')] * n

        # Build palindrome table (Bottom-Up DP)
        for length in range(1, n + 1):  # Length of substring
            for start in range(n - length + 1):  # Start index
                end = start + length - 1  # End index

                # Check if substring s[start:end+1] is a palindrome
                if s[start] == s[end] and (length == 1 or length == 2 or palindrome_table[start + 1][end - 1]):
                    palindrome_table[start][end] = True

        # Calculate minimum cuts
        for i in range(n):
            if palindrome_table[0][i]:
                cuts[i] = 0  # No cuts needed if s[0:i+1] is a palindrome
            else:
                for j in range(i):
                    if palindrome_table[j + 1][i]:
                        cuts[i] = min(cuts[i], cuts[j] + 1)

        return cuts[n - 1]