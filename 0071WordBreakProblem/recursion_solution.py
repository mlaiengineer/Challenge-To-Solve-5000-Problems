class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)                                              # Store the total length of the input string

        def check(index):

            # Base case: reached start of string, segmentation successful
            if index == 0:
                return True

            # Try every word in the dictionary at the current index
            for word in wordDict:
                word_length = len(word)                         # Get the length of the current dictionary word

                if index >= word_length:                        # Ensure slice does not go out of bounds
                    substring = s[index - word_length: index]   # Extract substring matching current word length

                    if substring == word and check(index - word_length):  # Check match and recurse left
                        return True

            return False                                        # No word matched at this index, return False

        return check(n)                                         # Start checking from end of the string