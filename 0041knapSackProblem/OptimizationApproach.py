def optimizationKnapsack(max_weight, weights, values, num_items):
    """
    Problem:
    Solve the 0/1 Knapsack Problem using an optimized dynamic programming approach 
    that reduces the space complexity. This solution uses only two arrays to store 
    results for the current and previous rows of the DP table.

    Inputs:
        - max_weight (int): The maximum weight capacity of the knapsack.
        - weights (list[int]): A list of weights for each item.
        - values (list[int]): A list of values for each item.
        - num_items (int): The number of items available.

    Output:
        - int: The maximum value that can be achieved without exceeding the weight limit.

    Example:
        Input:
            max_weight = 10
            weights = [2, 3, 5]
            values = [3, 2, 5]
            num_items = 3
        Output:
            8
        Explanation:
            The optimal solution includes the first and third items with weights 2 and 5, 
            and values 3 and 5, respectively, for a total value of 8.

    Time Complexity:
        - O(num_items * max_weight): We iterate through all items and all weight capacities.

    Space Complexity:
        - O(max_weight): We use two arrays of size `max_weight + 1`.
    """

    # Initialize two arrays to store results for the previous and current rows
    previous = [0] * (max_weight + 1)
    current = [0] * (max_weight + 1)

    # Iterate through all items
    for i in range(1, num_items + 1):
        # Iterate through all weight capacities
        for j in range(1, max_weight + 1):
            # Case 1: Exclude the current item
            exclude_item = previous[j]

            # Case 2: Include the current item (if weight allows)
            include_item = 0
            if weights[i - 1] <= j:
                include_item = values[i - 1] + previous[j - weights[i - 1]]

            # Update the current row with the maximum value
            current[j] = max(include_item, exclude_item)

        # Copy the current row to the previous row for the next iteration
        previous = current[:]

    # The final result is stored in the last entry of the current row
    return current[max_weight]


# Test Cases
if __name__ == "__main__":
    # Example 1
    max_weight = 10
    weights = [2, 3, 5]
    values = [3, 2, 5]
    num_items = len(weights)
    print("Maximum value:", optimizationKnapsack(max_weight, weights, values, num_items))  # Output: 8

    # Example 2
    max_weight = 7
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    num_items = len(weights)
    print("Maximum value:", optimizationKnapsack(max_weight, weights, values, num_items))  # Output: 9

    # Example 3
    max_weight = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    num_items = len(weights)
    print("Maximum value:", optimizationKnapsack(max_weight, weights, values, num_items))  # Output: 220
