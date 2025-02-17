public class TestSolution {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1: Array with some duplicates
        int[] nums1 = {1, 1, 2};
        System.out.println("Test Case 1: Unique count elements = " + solution.removeDuplicates(nums1));
        printArray(nums1);

        // Test case 2: Array with multiple duplicates
        int[] nums2 = {0, 0, 1, 1, 2, 2, 3, 3, 4};
        System.out.println("Test Case 2: Unique count elements = " + solution.removeDuplicates(nums2));
        printArray(nums2);

        // Test case 3: Array with all duplicates
        int[] nums3 = {1, 1, 1, 1};
        System.out.println("Test Case 3: Unique count elements = " + solution.removeDuplicates(nums3));
        printArray(nums3);

        // Test case 4: Array with all unique elements
        int[] nums4 = {1, 2, 3, 4, 5};
        System.out.println("Test Case 4: Unique count elements = " + solution.removeDuplicates(nums4));
        printArray(nums4);

        // Test case 5: Empty array
        int[] nums5 = {};
        System.out.println("Test Case 5: Unique count elements = " + solution.removeDuplicates(nums5));
        printArray(nums5);
    }

    // Helper method to print the array up to the unique elements
    private static void printArray(int[] nums) {
        System.out.print("Modified array: ");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
}