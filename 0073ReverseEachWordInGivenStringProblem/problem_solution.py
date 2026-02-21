class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()          # Split string into words, handles all extra spaces automatically
        reversed_s = ''                 # Initialize empty string to accumulate reversed words

        for word in words_list:
            reversed_s += word[::-1] + ' '  # Reverse each word and append with a space

        return reversed_s.strip()       # Remove trailing space before returning