def knapsack_max_value(num_items, max_weight, values, weights) -> int:
    """
    Solves the unbounded knapsack problem using a space-optimized tabulation approach.

    Args:
        num_items (int): Number of items available.
        max_weight (int): Maximum weight capacity of the knapsack.
        values (list): List of values for each item.
        weights (list): List of weights for each item.

    Returns:
        int: Maximum value obtainable with the given constraints.

    Time Complexity:
        O(N * W), where N is the number of items and W is the maximum weight capacity.
        For each item, we iterate through all capacities.

    Space Complexity:
        O(W), since we use a 1D array to store results for capacities up to `max_weight`.

    Explanation:
        - This approach builds the solution incrementally by considering each item and weight capacity.
        - The "space-optimization" lies in using a single 1D array (dp_table) instead of a 2D table.
    """
    
    # Initialize a DP table where dp_table[i] represents the maximum value for capacity i
    dp_table = [0] * (max_weight + 1)
    
    # Outer loop: Iterate through each available item to consider it for inclusion
    for item in range(num_items):
        # Inner loop: Update dp_table for all capacities that can include the current item
        for capacity in range(weights[item], max_weight + 1):
            # Update the DP table for the current capacity
            dp_table[capacity] = max(dp_table[capacity], values[item] + dp_table[capacity - weights[item]])
    
    # Return the maximum value obtainable for the full weight capacity
    return dp_table[max_weight]


if __name__ == "__main__":
    # Updated Test Case: New values and weights
    num_items = 4  # Number of items
    max_weight = 12  # Maximum weight capacity of the knapsack

    # Values of the items
    values = [10, 30, 20, 50]

    # Weights of the items
    weights = [3, 4, 5, 6]

    # Expected Output: 100
    # Explanation:
    #   - Take two of Item 4 (Value = 50, Weight = 6). Total value = 100, Total weight = 12.
    #   - Optimal combination: 2 × Item 4.
    print("Maximum Value:", knapsack_max_value(num_items, max_weight, values, weights))

    # Illustration:
    # Knapsack capacity = 12
    # Items considered:
    #   Item 1: Value = 10, Weight = 3
    #   Item 2: Value = 30, Weight = 4
    #   Item 3: Value = 20, Weight = 5
    #   Item 4: Value = 50, Weight = 6
    #
    # DP Table Evolution:
    # Capacity = 1: dp_table[1] = 0
    # Capacity = 3: dp_table[3] = 10 (one Item 1)
    # Capacity = 4: dp_table[4] = 30 (one Item 2)
    # Capacity = 6: dp_table[6] = 50 (one Item 4)
    # Capacity = 9: dp_table[9] = 60 (one Item 4 + one Item 1)
    # Capacity = 12: dp_table[12] = 100 (two Item 4)
