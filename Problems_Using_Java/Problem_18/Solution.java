class Solution {
    /**
     * Removes all occurrences of a specified value from the array in-place.
     *
     * This method modifies the input array such that the first k elements
     * are the elements that are not equal to the specified value. The order
     * of elements may change, and the remaining elements beyond k are not
     * relevant.
     *
     * @param nums The input array of integers.
     * @param val  The integer value to be removed from the array.
     * @return     The number of elements in nums that are not equal to val.
     */
    public int removeElement(int[] nums, int val) {
        // Initialize a variable k to 0 to count elements not equal to val.
        int k = 0;

        // Loop through each element in nums
        for (int num : nums) {
            if (num != val) {
                // Place it at index k in nums.
                nums[k] = num;
                k++;
            }
        }
        return k; // Return the count of elements not equal to val
    }
}