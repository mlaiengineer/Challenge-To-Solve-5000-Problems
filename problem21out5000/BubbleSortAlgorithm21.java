/**
 * Class Solution contains an implementation of the Bubble Sort algorithm.
 * 
 * Bubble Sort is a simple comparison-based sorting algorithm.
 * It repeatedly steps through the array, compares adjacent elements, and swaps them
 * if they are in the wrong order. This process is repeated until the array is sorted.
 * 
 * Time Complexity:
 *   - Best Case: O(n) (When the array is already sorted, due to the optimization flag)
 *   - Average Case: O(n²)
 *   - Worst Case: O(n²)
 * 
 * Space Complexity:
 *   - O(1) (In-place sorting, no additional memory required)
 * 
 * Stability:
 *   - Stable (The relative order of equal elements is preserved)
 * 
 * Usage:
 *   Useful for small datasets or when simplicity is preferred over efficiency.
 */
class Solution {

    /**
     * Function to sort the array using the Bubble Sort algorithm.
     * 
     * @param arr The array of integers to be sorted.
     */
    public static void bubbleSort(int arr[]) {
        int n = arr.length;

        // Outer loop for each pass through the array
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false; // Tracks if any elements were swapped during this pass

            // Inner loop to compare adjacent elements
            for (int j = 0; j < n - i - 1; j++) {
                // Compare and swap if the current element is greater than the next
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                    swapped = true; // Mark that a swap occurred
                }
            }

            // If no swaps occurred during this pass, the array is already sorted
            if (!swapped) {
                break;
            }
        }
    }
}
