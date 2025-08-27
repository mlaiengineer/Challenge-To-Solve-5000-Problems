def knapsack_max_value(num_items, max_weight, values, weights) -> int:
    """
    Solves the unbounded knapsack problem using memoization.

    Args:
        num_items (int): Number of items available.
        max_weight (int): Maximum weight capacity of the knapsack.
        values (list): List of values for each item.
        weights (list): List of weights for each item.

    Returns:
        int: Maximum value obtainable with the given constraints.

    Time Complexity:
        O(N * W), where N is the number of items and W is the maximum weight capacity.
        For each capacity, we iterate through all items.

    Space Complexity:
        O(W), due to the memoization table storing results for all capacities up to `max_weight`.
    """
    # Memoization table to store the maximum value for each capacity
    memo_table = [-1] * (max_weight + 1)

    def calculate_max_value(remaining_capacity) -> int:
        """
        Helper function to calculate the maximum value recursively with memoization.

        Args:
            remaining_capacity (int): Remaining weight capacity of the knapsack.

        Returns:
            int: Maximum value obtainable with the given remaining capacity.
        """
        # Base case: If the capacity is 0, no items can be added
        if remaining_capacity <= 0:
            return 0

        # If the result for the current capacity is already computed, return it
        if memo_table[remaining_capacity] != -1:
            return memo_table[remaining_capacity]

        # Track the best value for the current capacity
        max_value = 0

        # Iterate through all items to find the best possible value
        for i in range(num_items):
            if weights[i] <= remaining_capacity:
                # Include the current item and calculate the value for the remaining capacity
                current_value = values[i] + calculate_max_value(remaining_capacity - weights[i])
                # Update the maximum value
                max_value = max(max_value, current_value)

        # Store the result in the memoization table
        memo_table[remaining_capacity] = max_value
        return max_value

    # Start the calculation with the full knapsack capacity
    return calculate_max_value(max_weight)


# Example Test Case:
if __name__ == "__main__":
    # Number of items
    num_items = 4

    # Maximum weight capacity of the knapsack
    max_weight = 15

    # Values of the items
    values = [10, 40, 50, 70]

    # Weights of the items
    weights = [5, 4, 6, 8]

    # Expected output: 150
    # Explanation:
    #   - Take 2 of Item 4 (Value = 70, Weight = 8). Total value = 140, Total weight = 16.
    #   - Remove 1 unit of Item 4 and add Item 2 (Value = 40, Weight = 4).
    #   - Result: Two Items 2 and one 4 Value!
    print("Maximum Value:", knapsack_max_value(num_items, max_weight, values, weights))
