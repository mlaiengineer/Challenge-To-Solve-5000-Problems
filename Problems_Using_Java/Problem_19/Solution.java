/**
 * Solution class to remove duplicates from a sorted array.
 * Returns the number of unique elements and modifies the array in-place.
 * Time Complexity: O(n), Space Complexity: O(1)
 */
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        if (nums.length == 0) {
            return k; // Return 0 if the array is empty
        }

        k = 1; // Initialize k to 1 to represent the first unique element
        int lastUniqueElem = nums[0]; // Store the first element as the last unique element

        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != lastUniqueElem) { // Check if current element is unique
                nums[k] = nums[i]; // Store the unique element at the next position
                lastUniqueElem = nums[i]; // Update the last unique element
                k++; // Increment the count of unique elements
            }
        }

        return k; // Return the count of unique elements
    }
}
