class Solution:
    def find(self, arr, x):

        # Initialize result with -1 indicating x not found yet
        result = [-1, -1]
        # Pointer starting from the end to find last occurrence
        right_pointer = len(arr) - 1

        # Traverse array from both ends simultaneously
        for i in range(len(arr)):

            # Check if current element from left matches x and first occurrence not set yet
            if arr[i] == x and result[0] == -1:
                result[0] = i

            # Check if current element from right matches x and last occurrence not set yet
            if arr[right_pointer] == x and result[1] == -1:
                result[1] = right_pointer

            # Move right pointer one step to the left
            right_pointer -= 1

            # Early exit if both occurrences are found
            if result[0] != -1 and result[1] != -1:
                break

        return result

