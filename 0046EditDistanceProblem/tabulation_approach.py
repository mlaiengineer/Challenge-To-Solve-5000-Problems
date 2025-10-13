class Solution(object):
    def minDistance(self, word1, word2):
        """
        Calculates the minimum number of operations required to convert word1 to word2
        using a tabulation (bottom-up dynamic programming) approach.

        Operations allowed:
        1. Insert a character.
        2. Delete a character.
        3. Replace a character.

        :type word1: str
        :type word2: str
        :rtype: int

        Approach:
        - Use a 2D DP table where dp_table[i][j] represents the minimum edit distance
          between the first i characters of word1 and the first j characters of word2.
        - Base cases:
          - When one string is empty, the edit distance equals the length of the other string.
        - Transition:
          - If word1[i-1] == word2[j-1], no operation is needed, so dp_table[i][j] = dp_table[i-1][j-1].
          - Otherwise, consider the minimum of:
            1. Replace a character: dp_table[i-1][j-1] + 1.
            2. Delete a character: dp_table[i-1][j] + 1.
            3. Insert a character: dp_table[i][j-1] + 1.
        - Return the value at dp_table[n][m], where n and m are the lengths of word1 and word2 respectively.
        """

        # Step 1: Compute the lengths of both words
        n = len(word1)
        m = len(word2)

        # Step 2: Initialize the DP table with dimensions (n+1) x (m+1)
        # dp_table[i][j] will store the minimum edit distance for word1[:i] and word2[:j]
        dp_table = [[0] * (m + 1) for _ in range(n + 1)]

        # Step 3: Fill the first row and first column (base cases)
        for j in range(m + 1):
            dp_table[0][j] = j  # Converting an empty word1 to word2[:j] requires j insertions
        for i in range(n + 1):
            dp_table[i][0] = i  # Converting word1[:i] to an empty word2 requires i deletions

        # Step 4: Fill the DP table for all rows and columns
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If characters are the same, no additional operation is needed
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    # If characters are different, consider all three operations:
                    # 1. Replace the character
                    replace = dp_table[i - 1][j - 1] + 1
                    # 2. Delete a character from word1
                    delete = dp_table[i - 1][j] + 1
                    # 3. Insert a character into word1
                    insert = dp_table[i][j - 1] + 1

                    # Take the minimum of the three operations
                    dp_table[i][j] = min(replace, delete, insert)

        # Step 5: Return the result stored in dp_table[n][m],
        # which represents the edit distance between the entire word1 and word2
        return dp_table[n][m]


# Test cases to validate the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Both words are empty
    word1 = ""
    word2 = ""
    print(f"Edit distance between '{word1}' and '{word2}': {solution.minDistance(word1, word2)}")
    # Expected output: 0

    # Test case 2: One word is empty
    word1 = "abc"
    word2 = ""
    print(f"Edit distance between '{word1}' and '{word2}': {solution.minDistance(word1, word2)}")
    # Expected output: 3

    # Test case 3: General case with different lengths
    word1 = "horse"
    word2 = "ros"
    print(f"Edit distance between '{word1}' and '{word2}': {solution.minDistance(word1, word2)}")
    # Expected output: 3
