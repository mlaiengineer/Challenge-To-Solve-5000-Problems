def combine(n, k):
    """
    Complexity Analysis:
    --------------------
    - Time Complexity: O(k * C(n, k))
      Each valid combination requires O(k) time to copy (where k is the combination size) and the
      number of valid combinations is C(n, k). Thus, the overall time complexity is O(k * C(n, k)).
    - Space Complexity: O(k)
      The depth of the recursion tree is at most k (the size of the combination), and we store one combination
      at each level.
    """
    
    result = []

    def backtracking(start, combine):
        # Base case: when the current combination has k numbers, add it to the result.
        if len(combine) == k:
            result.append(combine[:])  # Create a shallow copy to ensure list integrity.
            return

        # Iterate through possible candidates starting from 'start'
        for j in range(start, n + 1):
            combine.append(j)  # Choose: add the candidate to the combination.
            backtracking(j + 1, combine)  # Explore: move to the next candidate.
            combine.pop()  # Un-choose: remove the last element to backtrack.

    # Start building combinations from 1
    backtracking(1, [])
    return result

# Example usage and test cases:
print("Test Case 1 - combine(4, 2):", combine(4, 2))
#Expacted ouput:  [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print("Test Case 2 - combine(5, 3):", combine(5, 3))
#Expacted output:[[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]

print("Test Case 3 - combine(3, 1):", combine(3, 1))
#Expacted output:  [[1], [2], [3]]
