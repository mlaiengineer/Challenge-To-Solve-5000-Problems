class Solution:
    def count(self, s):

        even_count = 0  # Tracks number of characters with even frequency
        char_frequency = {}  # Maps each character to its occurrence count

        for char in s:
            if char not in char_frequency:
                char_frequency[char] = 1  # Initialize character frequency to 1 on first encounter
            else:
                char_frequency[char] += 1  # Increment frequency for already seen character

        for char, frequency in char_frequency.items():
            if frequency % 2 == 0:  # Check if character frequency is divisible by 2
                even_count += 1  # Increment counter if frequency is even

        return even_count  # Return total distinct characters with even frequency