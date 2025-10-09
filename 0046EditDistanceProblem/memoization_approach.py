class Solution(object):
    def minDistance(self, word1, word2):
        """
        Calculates the minimum number of operations required to convert word1 to word2.
        Operations allowed: insert a character, delete a character, or replace a character.

        :type word1: str
        :type word2: str
        :rtype: int

        Approach:
        - Use recursion with memoization to avoid redundant computations for overlapping subproblems.
        - The recursive function explores all possible operations (insert, delete, replace) at each step.
        - Base cases handle when one or both strings are empty.
        - A memoization table is used to store results of previously computed states (index1, index2).
        """

        n = len(word1)  # Length of the first word
        m = len(word2)  # Length of the second word
        # Initialize a memoization table with -1 (indicating uncomputed states)
        memo_table = [[-1] * m for _ in range(n)]

        # Helper function to perform recursion
        def recursion(index1, index2):
            """
            Recursively computes the minimum edit distance between substrings of word1 and word2.

            :param index1: Current index in word1
            :param index2: Current index in word2
            :return: Minimum edit distance between word1[index1:] and word2[index2:]
            """

            # Base cases
            if index1 >= n and index2 >= m:
                return 0  # Both strings are empty, no operations needed
            if index1 >= n:
                return m - index2  # Remaining characters in word2 need to be inserted
            if index2 >= m:
                return n - index1  # Remaining characters in word1 need to be deleted

            # Check if the result is already computed in the memoization table
            if memo_table[index1][index2] != -1:
                return memo_table[index1][index2]

            # Recursive case
            if word1[index1] == word2[index2]:
                # If the current characters are the same, no operation is needed; move to the next characters
                memo_table[index1][index2] = recursion(index1 + 1, index2 + 1)
            else:
                # If characters are different, consider all possible operations:
                # 1. Replace the character at index1 in word1 with the character at index2 in word2
                # 2. Delete the character at index1 in word1
                # 3. Insert the character at index2 in word2 at index1 in word1
                # Return the minimum of these three operations +1 (for the current operation)
                replace = recursion(index1 + 1, index2 + 1)  # Replace operation
                delete = recursion(index1 + 1, index2)      # Delete operation
                insert = recursion(index1, index2 + 1)      # Insert operation

                # Store the result in the memoization table
                memo_table[index1][index2] = 1 + min(replace, delete, insert)

            return memo_table[index1][index2]

        # Start the recursion from the beginning of both words
        return recursion(0, 0)


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
