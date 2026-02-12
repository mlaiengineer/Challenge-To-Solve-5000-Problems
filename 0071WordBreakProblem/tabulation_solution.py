"""
LeetCode 139: Word Break
Difficulty: Medium

Problem Description:
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Determines if a string can be segmented into words from a dictionary.

        Approach: Dynamic Programming with 2D Table
        - Uses a 2D DP table where dp_table[start][end] represents whether 
          the substring s[start:end+1] can be segmented using words from wordDict
        - Builds solutions bottom-up by increasing substring length

        :type s: str - The input string to segment
        :type wordDict: List[str] - List of valid dictionary words
        :rtype: bool - True if s can be segmented, False otherwise
        """

        # Get the length of the input string
        string_length = len(s)

        # Initialize a 2D DP table with False values
        # dp_table[start][end] = True if substring s[start:end+1] can be segmented
        dp_table = [[False] * string_length for _ in range(string_length)]

        # Iterate through all possible substring lengths (1 to string_length)
        for current_length in range(1, string_length + 1):

            # Iterate through all possible starting positions for current substring length
            for start_index in range(string_length - current_length + 1):

                # Calculate the ending index for the current substring
                end_index = start_index + current_length - 1

                # Extract the current substring from start_index to end_index (inclusive)
                current_substring = s[start_index:end_index + 1]

                # Check if the entire current substring exists in the word dictionary
                if current_substring in wordDict:
                    # Mark this substring as valid (can be segmented)
                    dp_table[start_index][end_index] = True
                else:
                    # Try to split the substring into two parts and check if both can be segmented
                    # Iterate through all possible split points within the current substring
                    for split_point in range(start_index, end_index):

                        # Check if we can split at 'split_point':
                        # - Left part: s[start_index:split_point+1] must be valid
                        # - Right part: s[split_point+1:end_index+1] must be valid
                        left_part_valid = dp_table[start_index][split_point]
                        right_part_valid = dp_table[split_point + 1][end_index]

                        # If both parts are valid, the entire substring is valid
                        if left_part_valid and right_part_valid:
                            dp_table[start_index][end_index] = True
                            break  # No need to check further split points

        # Return whether the entire string (from index 0 to string_length-1) can be segmented
        return dp_table[0][string_length - 1]


"""
COMPLEXITY ANALYSIS:
===================

Time Complexity: O(n³)
- Outer loop iterates through all substring lengths: O(n)
- Middle loop iterates through all starting positions: O(n)
- Inner loop (for split points) can iterate up to n times: O(n)
- Substring extraction s[start:end+1] takes O(n) in worst case
- Dictionary lookup is O(1) on average with hash set
- Overall: O(n) * O(n) * O(n) = O(n³)

Space Complexity: O(n²)
- 2D DP table of size n × n: O(n²)
- Substring creation can take O(n) space temporarily
- Overall space: O(n²)

where n = length of input string s
"""