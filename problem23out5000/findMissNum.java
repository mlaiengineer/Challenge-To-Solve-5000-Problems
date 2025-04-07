/**
 * Solution to find the missing number in an array of n distinct integers in the range [0, n].
 * The approach uses the mathematical formula for the sum of the first n natural numbers.
 *
 * Time Complexity: O(n) - Single pass through the array.
 * Space Complexity: O(1) - Constant space usage.
 */
class Solution {
    /**
     * Finds the missing number in the given array.
     *
     * @param nums The input array containing n distinct numbers in the range [0, n].
     * @return The missing number in the range [0, n].
     */
    public int missingNumber(int[] nums) {
        // Step 1: Get the size of the array
        int n = nums.length;

        // Step 2: Calculate the expected sum of numbers in the range [0, n]
        // Formula for the sum: n * (n + 1) / 2
        int expectedSum = n * (n + 1) / 2;

        // Step 3: Calculate the actual sum of the elements in the array
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num; // Accumulate the sum of elements in nums
        }

        // Step 4: The missing number is the difference between the expected and actual sums
        return expectedSum - actualSum;
    }
}
