// ✅ Class Definition: This class contains the solution to search an element in a sorted array.
class Solution {

    /**
     * 🔍 Method to search an element in a sorted array.
     * @param arr The sorted array in which we want to search.
     * @param k The element to search for.
     * @return true if the element is found, false otherwise.
     *
     * 📌 Time Complexity: O(n) – Linear search in a sorted array.
     * ⚠️ Note: Although the array is sorted, this approach uses a brute force linear search.
     *          For better performance on large datasets, consider Binary Search (O(log n)).
     */
    static boolean searchInSorted(int arr[], int k) {

        // 🔁 Iterate over each element of the array
        for (int i = 0; i < arr.length; i++) {

            // ✅ Check if the current element matches the target value
            if (arr[i] == k) {
                return true; // 🎯 Target found, return true
            }
        }

        // ❌ Target element was not found in the array
        return false;
    }
}
