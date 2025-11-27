class Solution:
    """
    Finds the position (0-based index) of k in the sorted array arr using binary search.
    If multiple occurrences exist, it returns the smallest index.
    If k is not found, it returns -1.
    Time Complexity: O(log N)
    """

    def binarysearch(self, arr: list[int], k: int) -> int:
        # Initialize the search boundaries.
        low = 0
        high = len(arr) - 1
        # Variable to store the potential result index. Initialize to -1 (not found).
        result_index = -1

        # The core binary search loop continues as long as the search space is valid.
        while low <= high:
            # Calculate the middle index. Using low + (high - low) // 2 prevents
            # potential integer overflow compared to (low + high) // 2.
            mid = low + (high - low) // 2

            if arr[mid] == k:
                # 1. Found an occurrence of k.
                # Store this index as a potential result.
                result_index = mid

                # 2. Key step for finding the *smallest* index:
                # Since the array is sorted, any smaller index for k must be in the
                # left half (arr[low...mid-1]). So, we discard the right half.
                high = mid - 1

            elif arr[mid] < k:
                # The target k must be in the right half (arr[mid+1...high]).
                low = mid + 1
            else:  # arr[mid] > k
                # The target k must be in the left half (arr[low...mid-1]).
                high = mid - 1

        # Return the index of the first occurrence found, or -1 if never found.
        return result_index


# --- Test Cases ---
test_solution = Solution()
print(f"Test 1: [1, 2, 3], k=3 -> Expected: 2, Got: {test_solution.binarysearch([1, 2, 3], 3)}")
# Output: 2

print(f"Test 2: [1, 2, 2, 3, 4], k=5 -> Expected: -1, Got: {test_solution.binarysearch([1, 2, 2, 3, 4], 5)}")
# Output: -1

print(
    f"Test 3 (Multiple Occurrences): [1, 2, 2, 2, 4], k=2 -> Expected: 1, Got: {test_solution.binarysearch([1, 2, 2, 2, 4], 2)}")
# Output: 1 (Ensures smallest index is returned)