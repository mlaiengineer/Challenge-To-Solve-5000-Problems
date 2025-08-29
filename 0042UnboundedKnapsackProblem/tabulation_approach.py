def knapsack_max_value(num_items, max_weight, values, weights) -> int:
    """
    Solves the unbounded knapsack problem using tabulation (bottom-up dynamic programming).

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
        O(W), since we use a 1D array (dp_table) to store results for capacities up to `max_weight`.
    """
    # Initialize a DP table where dp_table[i] represents the maximum value for capacity i
    dp_table = [0] * (max_weight + 1)

    # Iterate through all capacities from 1 to max_weight
    for capacity in range(1, max_weight + 1):
        # Check each item to see if it can fit into the current capacity
        for item in range(num_items):
            # If the item's weight is less than or equal to the current capacity
            if weights[item] <= capacity:
                # Update the DP table with the maximum value achievable at this capacity
                dp_table[capacity] = max(dp_table[capacity], values[item] + dp_table[capacity - weights[item]])

    # The result for the full weight capacity is stored at dp_table[max_weight]
    return dp_table[max_weight]


if __name__ == "__main__":
    # Test Case: Changed values and weights
    num_items = 3  # Number of items
    max_weight = 10  # Maximum weight capacity of the knapsack

    # Values of the items
    values = [15, 25, 45]

    # Weights of the items
    weights = [2, 3, 5]

    # Expected Output: 90
    # Explanation:
    #   - Take two of Item 3 (Value = 45, Weight = 5). Total value = 90, Total weight = 10.
    #   - Optimal combination: 2 × Item 3.
    print("Maximum Value:", knapsack_max_value(num_items, max_weight, values, weights))

    # Illustration:
    # Knapsack capacity = 10
    # Items considered:
    #   Item 1: Value = 15, Weight = 2
    #   Item 2: Value = 25, Weight = 3
    #   Item 3: Value = 45, Weight = 5
    #
    # DP Table Evolution:
    # Capacity = 1: dp_table[1] = 0
    # Capacity = 2: dp_table[2] = 15 (one Item 1)
    # Capacity = 3: dp_table[3] = 25 (one Item 2)
    # Capacity = 5: dp_table[5] = 45 (one Item 3)
    # Capacity = 10: dp_table[10] = 90 (two Item 3)
