class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        🔹 Problem: Longest Common Subsequence (LCS)
        -------------------------------------------------
        Given two strings, find the length of the longest subsequence 
        common to both strings. A subsequence is formed by deleting 
        some (or none) characters without changing the order of the remaining characters.
        """
        # Get the lengths of both input strings
        length_text1 = len(text1)
        length_text2 = len(text2)

        # Initialize the DP table with zeros
        # dp_table[i][j] represents the LCS length of text1[0:i] and text2[0:j]
        dp_table = [[0] * (length_text2 + 1) for _ in range(length_text1 + 1)]

        # Fill the DP table iteratively
        for i in range(1, length_text1 + 1):
            for j in range(1, length_text2 + 1):
                # If characters match, extend the LCS
                if text1[i - 1] == text2[j - 1]:
                    dp_table[i][j] = 1 + dp_table[i - 1][j - 1]
                else:
                    # If characters don't match, take the maximum LCS by skipping one character
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

        # The final result is stored in dp_table[length_text1][length_text2]
        return dp_table[length_text1][length_text2]


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
