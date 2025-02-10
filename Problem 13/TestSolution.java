/**
 * Test cases to validate the implementation of the longestUniqueSubstring() method.
 * Each test case covers different edge cases to ensure correctness.
 */
public class TestSolution {
    public static void main(String[] args) {
        // Create an instance of the Solution class
        Solution s = new Solution();

        // 📌 Test Case 1: String with repeated characters (All same characters)
        System.out.println("Test 1 | Input: \"aaaaa\" | Expected: 1 | Output: "
                + s.longestUniqueSubstring("aaaaa"));

        // 📌 Test Case 2: String with two different characters
        System.out.println("Test 2 | Input: \"ab\" | Expected: 2 | Output: "
                + s.longestUniqueSubstring("ab"));

        // 📌 Test Case 3: Empty string (Edge case)
        System.out.println("Test 3 | Input: \"\" | Expected: 0 | Output: "
                + s.longestUniqueSubstring(""));

        // 📌 Test Case 4: Single space character (Edge case)
        System.out.println("Test 4 | Input: \" \" | Expected: 1 | Output: "
                + s.longestUniqueSubstring(" "));

        // 📌 Test Case 5: A long string with repeating patterns and spaces
        System.out.println("Test 5 | Input: \"abcabcabcabc def\" | Expected: 7 | Output: "
                + s.longestUniqueSubstring("abcabcabcabc def"));
    }
}
