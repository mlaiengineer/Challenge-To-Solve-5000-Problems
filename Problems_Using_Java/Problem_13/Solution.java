import java.util.Arrays;

class Solution {
    /**
     * Finds the length of the longest substring with unique characters
     * using the sliding window technique.
     *
     * @param s The input string
     * @return The length of the longest unique substring
     */
    public int longestUniqueSubstring(String s) {
        // Variable to store the maximum length of the substring
        int maxLength = 0;

        // Array to store the last index of each ASCII character (256 possible characters)
        int[] lastIndex = new int[256];

        // Initialize all values in lastIndex to -1
        Arrays.fill(lastIndex, -1);

        // Left and right pointers to track the current window of unique characters
        int left = 0, right = 0;

        // Iterate through the string using the right pointer
        for (right = 0; right < s.length(); right++) {
            // If the character has appeared before within the window, update the left pointer
            if (lastIndex[s.charAt(right)] != -1) {
                // Ensure the window only contains unique characters
                left = Math.max(left, lastIndex[s.charAt(right)] + 1);
            }

            // Update the maximum length found so far
            maxLength = Math.max(maxLength, right - left + 1);

            // Update the last occurrence of the current character
            lastIndex[s.charAt(right)] = right;
        }

        // Return the length of the longest unique substring
        return maxLength;
    }
}
