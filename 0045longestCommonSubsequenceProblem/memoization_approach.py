class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        🔹 Problem: Longest Common Subsequence (LCS)
        -------------------------------------------------
        Given two strings, find the length of the longest subsequence 
        common to both strings. A subsequence is formed by deleting 
        some (or none) characters without changing the order of the remaining characters.

        🧠 Approach: Top-Down Dynamic Programming (Memoization)
        -------------------------------------------------
        - Use recursion to explore all subsequences.
        - Store already computed results in a memo table to avoid recomputation.
        """

        # Get lengths of both input strings
        length_text1 = len(text1)
        length_text2 = len(text2)

        # Create a memoization table initialized with -1
        # Dimensions: [length_text1][length_text2]
        # memo_table[i][j] will store the LCS length for substrings text1[i:] and text2[j:]
        memo_table = [[-1] * length_text2 for _ in range(length_text1)]

        def find_lcs(index1, index2):
            """
            🧩 Recursive helper function to compute LCS length starting from indices (index1, index2)
            
            Args:
                index1 (int): Current position in text1
                index2 (int): Current position in text2
            
            Returns:
                int: LCS length from text1[index1:] and text2[index2:]
            """

            # 🛑 Base Case:
            # If we reach the end of either string, no more subsequence can be formed
            if index1 >= length_text1 or index2 >= length_text2:
                return 0

            # ✅ If the result is already computed, return it (Memoization)
            if memo_table[index1][index2] != -1:
                return memo_table[index1][index2]

            # 🎯 Case 1: Characters match → part of LCS
            if text1[index1] == text2[index2]:
                # Include this character and move diagonally in both strings
                memo_table[index1][index2] = 1 + find_lcs(index1 + 1, index2 + 1)
            
            else:
                # 🎯 Case 2: Characters don’t match → explore both possibilities:
                # Option 1: Move forward in text1, keep text2 fixed
                # Option 2: Move forward in text2, keep text1 fixed
                # Take the maximum of both options
                option1 = find_lcs(index1 + 1, index2)
                option2 = find_lcs(index1, index2 + 1)
                memo_table[index1][index2] = max(option1, option2)

            # Return the computed result for this subproblem
            return memo_table[index1][index2]

        # 🏁 Start recursion from the beginning of both strings
        return find_lcs(0, 0)


# 🧪 Test cases
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
