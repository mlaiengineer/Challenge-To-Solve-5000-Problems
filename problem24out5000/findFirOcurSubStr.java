/**
 * Solution class for finding the first occurrence of a substring (needle) 
 * within a given string (haystack).
 * 
 * This implementation uses a sliding window approach to compare substrings 
 * of the haystack with the needle. If a match is found, the starting index 
 * of the match is returned. Otherwise, -1 is returned.
 */
class Solution {

    /**
     * Finds the index of the first occurrence of needle in haystack, 
     * or returns -1 if needle is not part of haystack.
     *
     * @param haystack The string in which to search for the substring.
     * @param needle   The substring to search for.
     * @return The index of the first occurrence of needle in haystack, or -1 if not found.
     */
    public int strStr(String haystack, String needle) {
        
        // Check for edge case: if needle is empty, return 0 as per the problem's requirements
        if (needle.isEmpty()) {
            return 0;
        }
        
        // If the needle is longer than the haystack, it cannot be found
        if (needle.length() > haystack.length()) {
            return -1;
        }
        
        int needleLength = needle.length();
        
        // Loop through haystack, checking substrings of length equal to needle
        for (int i = 0; i <= haystack.length() - needleLength; i++) {
            // If a matching substring is found, return the starting index
            if (haystack.substring(i, i + needleLength).equals(needle)) {
                return i;
            }
        }
        
        // If no match is found, return -1
        return -1;
    }
}
// TestSolution 
public class SolutionTest {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test cases
        System.out.println(solution.strStr("sadbutsad", "sad")); // Expected: 0
        System.out.println(solution.strStr("leetcode", "leeto")); // Expected: -1
        System.out.println(solution.strStr("hello", "ll")); // Expected: 2
        System.out.println(solution.strStr("aaaaa", "bba")); // Expected: -1
        System.out.println(solution.strStr("", "")); // Expected: 0
    }
}
