class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        🔹 Problem: Longest Common Subsequence (LCS)
        -------------------------------------------------
        Given two strings, find the length of the longest subsequence 
        common to both strings. A subsequence is formed by deleting 
        some (or none) characters without changing the order of the remaining characters.

        🧠 Approach: Space-Optimized Dynamic Programming
        -------------------------------------------------
        - Instead of using a full 2D DP table, maintain only two 1D arrays:
          `previous` (representing the previous row) and `current` (representing the current row).
        - Use these arrays to iteratively compute LCS values for the current row based on the previous row.
        - If characters match, extend the LCS:
          `current[j] = 1 + previous[j-1]`.
        - If characters don't match, take the maximum LCS from the previous row:
          `current[j] = max(previous[j], current[j-1])`.
        - At the end of each row computation, copy `current` into `previous` for the next iteration.

        🕒 Complexity:
        -------------------------------------------------
        - **Time Complexity**: O(n * m), where `n` and `m` are the lengths of `text1` and `text2`.
          Each cell in the DP table is computed once.
        - **Space Complexity**: O(m), where `m` is the length of `text2`.
          Only two 1D arrays of size `m+1` are used for computation.

        🚀 Example:
        -------------------------------------------------
        text1 = "abcde", text2 = "ace" → LCS = "ace", length = 3
        """

        # Get the lengths of both input strings
        length_text1 = len(text1)
        length_text2 = len(text2)

        # Initialize two rows for the DP table
        previous = [0] * (length_text2 + 1)  # Represents the previous row
        current = [0] * (length_text2 + 1)   # Represents the current row

        # Fill the DP table iteratively
        for i in range(1, length_text1 + 1):
            for j in range(1, length_text2 + 1):
                # If characters match, extend the LCS
                if text1[i - 1] == text2[j - 1]:
                    current[j] = 1 + previous[j - 1]
                else:
                    # If characters don't match, take the max LCS from previous computations
                    current[j] = max(previous[j], current[j - 1])

            # Update 'previous' row for the next iteration
            previous = current[:]

        # The LCS length is stored in the last cell of the current row
        return current[length_text2]


# 🧪 Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Common subsequence is "ace" → length 3
    text1 = "abcde"
    text2 = "ace"
    print("Test Case 1 Result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 3

    # Test Case 2: No common characters → length 0
    text1 = "abc"
    text2 = "def"
    print("Test Case 2 Result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 0

    # Test Case 3: Identical strings → entire string is LCS
    text1 = "abc"
    text2 = "abc"
    print("Test Case 3 Result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 3

    # Test Case 4: One string is empty → LCS length is 0
    text1 = "abc"
    text2 = ""
    print("Test Case 4 Result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 0

    # Test Case 5: Both strings are empty → LCS length is 0
    text1 = ""
    text2 = ""
    print("Test Case 5 Result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 0
