public class TestSolution {
    public static void main(String[] args) {
        /**
         * This class contains the main method to test the reverseString method.
         */
        // Test case 1: Regular string
        String case1 = "hello";
        System.out.println("Input: " + case1 + " | Reversed: " + Solution.reverseString(case1));

        // Test case 2: Palindrome string (should return the same string)
        String case2 = "racecar";
        System.out.println("Input: " + case2 + " | Reversed: " + Solution.reverseString(case2));

        // Test case 3: Empty string (should return an empty string)
        String case3 = "";
        System.out.println("Input: \"" + case3 + "\" | Reversed: \"" + Solution.reverseString(case3) + "\"");

        // Test case 4: Single character string (should return the same character)
        String case4 = "A";
        System.out.println("Input: " + case4 + " | Reversed: " + Solution.reverseString(case4));

        // Test case 5: String with spaces and punctuation
        String case5 = "Hello, World!";
        System.out.println("Input: " + case5 + " | Reversed: " + Solution.reverseString(case5));
    }
}
