class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        Finds the length of the longest common subsequence between two strings.

        :param text1: str, the first input string
        :param text2: str, the second input string
        :return: int, the length of the longest common subsequence
        """
        # Get the lengths of both input strings
        length_text1 = len(text1)
        length_text2 = len(text2)

        def find_lcs(index1, index2):
            """
            A recursive helper function to find the LCS length.

            :param index1: int, current index in text1
            :param index2: int, current index in text2
            :return: int, the length of the LCS from these indices onward
            """
            # Base case: if we reach the end of either string, return 0
            if index1 >= length_text1 or index2 >= length_text2:
                return 0

            # If characters match, include them in the LCS and move to the next indices
            if text1[index1] == text2[index2]:
                return 1 + find_lcs(index1 + 1, index2 + 1)

            # If characters don't match, explore both possible paths:
            # 1. Skip the current character in text1
            # 2. Skip the current character in text2
            # Take the maximum of both options
            return max(find_lcs(index1 + 1, index2), find_lcs(index1, index2 + 1))

        # Start the recursion from the beginning of both strings
        return find_lcs(0, 0)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example with matching subsequence
    text1 = "abcde"
    text2 = "ace"
    print("Test case 1 result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 3 ("ace")

    # Test case 2: No common subsequence
    text1 = "abc"
    text2 = "def"
    print("Test case 2 result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 0

    # Test case 3: One string is a subsequence of the other
    text1 = "abc"
    text2 = "abc"
    print("Test case 3 result:", solution.longestCommonSubsequence(text1, text2))  # Expected: 3 ("abc")
