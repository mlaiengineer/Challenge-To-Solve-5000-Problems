/**
 * This method reverses the characters in a given string.
 * For instance, if the input string is "hello", the output will be "olleh".
 *
 * @param s The input string to be reversed.
 * @return A new string that is the reverse of the input string.
 *         Note: This method handles null and empty strings gracefully.
 */
class Solution {
    public static String reverseString(String s) {
        // Initialize a StringBuilder to construct the reversed string
        StringBuilder reversedString = new StringBuilder();

        // Iterate through the input string in reverse order
        for (int i = s.length() - 1; i >= 0; i--) {
            // Append each character from the end of the string to the StringBuilder
            reversedString.append(s.charAt(i));
        }

        // Convert the StringBuilder to a string and return the reversed string
        return reversedString.toString();
    }
}