/**
 * Class Solution contains an implementation of the Selection Sort algorithm.
 * 
 * Selection Sort is an in-place comparison-based sorting algorithm.
 * It repeatedly selects the smallest element from the unsorted portion of the array 
 * and places it at the correct position in the sorted portion.
 * 
 * Time Complexity:
 *   - Best Case: O(n^2) (No optimization for already sorted arrays)
 *   - Average Case: O(n^2)
 *   - Worst Case: O(n^2)
 * 
 * Space Complexity:
 *   - O(1) (In-place sorting, no extra memory used)
 * 
 * Stability:
 *   - Not Stable (The relative order of equal elements may not be preserved)
 * 
 * Usage:
 *   This algorithm is simple to implement but inefficient for large datasets. 
 *   It is primarily used for educational purposes or when memory usage is a concern.
 */
class Solution {
    /**
     * Performs in-place Selection Sort on the input array.
     * 
     * @param arr The array of integers to be sorted.
     */
    void selectionSort(int[] arr) {
        int length = arr.length;

        // Outer loop iterates over the unsorted part of the array
        for (int i = 0; i < length - 1; i++) {
            int indexOfMinEle = i; // Assume the current position has the smallest element

            // Inner loop to find the smallest element in the remaining unsorted part
            for (int j = i + 1; j < length; j++) {
                if (arr[j] < arr[indexOfMinEle]) {
                    indexOfMinEle = j; // Update indexOfMinEle to the new minimum
                }
            }

            // Swap the smallest element found with the element at the current position
            if (indexOfMinEle != i) {
                int temp = arr[i];
                arr[i] = arr[indexOfMinEle];
                arr[indexOfMinEle] = temp;
            }
        }
    }
}
