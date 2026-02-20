class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)                                              # Store the total length of the input string
        dp_table = [-1] * (n + 1)                              # Size n+1 to allow index access up to n

        def check(index):

            # Base case: reached start of string, segmentation successful
            if index == 0:
                return True

            # Return cached result if this index was already computed
            if dp_table[index] != -1:
                return dp_table[index]

            # Try every word in the dictionary at the current index
            for word in wordDict:
                word_length = len(word)                         # Get the length of the current dictionary word

                if index >= word_length:                        # Ensure slice does not go out of bounds
                    substring = s[index - word_length: index]   # Extract substring matching current word length

                    if substring == word and check(index - word_length):  # Check match and recurse left
                        dp_table[index] = True                  # Cache the result as True before returning
                        return dp_table[index]

        # No word matched at this index, cache and return False
            dp_table[index] = False
            return dp_table[index]

        return check(n)                                         # Start checking from end of the string