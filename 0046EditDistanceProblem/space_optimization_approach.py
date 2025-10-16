class Solution(object):
    def minDistance(self, word1, word2):
        """
        Calculates the minimum number of operations required to convert word1 to word2
        using a space-optimized dynamic programming approach.

        Operations allowed:
        1. Insert a character.
        2. Delete a character.
        3. Replace a character.

        :type word1: str
        :type word2: str
        :rtype: int

        Approach:
        - Use two 1D arrays (`prev_row` and `curr_row`) to store the results of the previous
          and current rows of the DP table, reducing space complexity to O(m).
        - Transition:
          - If word1[i-1] == word2[j-1], no operation is needed: curr_row[j] = prev_row[j-1].
          - Otherwise, consider the minimum of:
            1. Replace: 1 + prev_row[j-1].
            2. Delete: 1 + prev_row[j].
            3. Insert: 1 + curr_row[j-1].
        - The result is stored in the last cell of `prev_row` after processing all rows.

        Time Complexity: O(m * n)
        Space Complexity: O(m)
        """

        n = len(word1)  # Length of word1
        m = len(word2)  # Length of word2

        # Step 1: Initialize two arrays to represent the previous and current rows
        prev_row = [0] * (m + 1)  # Stores results of the previous row
        curr_row = [0] * (m + 1)  # Stores results of the current row

        # Step 2: Fill the first row (base case: converting "" to word2[:j])
        for j in range(m + 1):
            prev_row[j] = j

        # Step 3: Fill the DP table row by row
        for i in range(1, n + 1):
            # Initialize the first column (base case: converting word1[:i] to "")
            curr_row[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If characters are the same, no operation is needed
                    curr_row[j] = prev_row[j - 1]
                else:
                    # Otherwise, consider all operations: replace, delete, and insert
                    replace = 1 + prev_row[j - 1]
                    delete = 1 + prev_row[j]
                    insert = 1 + curr_row[j - 1]
                    curr_row[j] = min(replace, delete, insert)
            # Move to the next row: update prev_row to be the current row
            prev_row = curr_row[:]

        # Step 4: Return the result in the last cell of the last processed row
        return prev_row[m]


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
