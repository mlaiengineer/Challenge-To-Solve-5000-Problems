def knapsack_max_value(num_items, max_weight, values, weights) -> int:
    """
    Solves the unbounded knapsack problem using recursion.

    Args:
        num_items (int): Number of items available.
        max_weight (int): Maximum weight capacity of the knapsack.
        values (list): List of values for each item.
        weights (list): List of weights for each item.

    Returns:
        int: Maximum value obtainable with the given constraints.
    """

    def calculate_max_value(remaining_capacity) -> int:
        """
        Helper function to calculate the maximum value recursively.

        Args:
            remaining_capacity (int): Remaining weight capacity of the knapsack.

        Returns:
            int: Maximum value obtainable with the given remaining capacity.
        """
        # Base case: No capacity left
        if remaining_capacity <= 0:
            return 0

        # Track the best value found so far
        max_value = 0

        # Iterate through all items to find the best possible value
        for i in range(num_items):
            if weights[i] <= remaining_capacity:
                # Include the current item and subtract its weight
                current_value = values[i] + calculate_max_value(remaining_capacity - weights[i])
                # Update the maximum value
                max_value = max(max_value, current_value)

        return max_value

    # Start the calculation with the full knapsack capacity
    return calculate_max_value(max_weight)


# Example Test Case:
if __name__ == "__main__":
    # Number of items
    num_items = 3

    # Maximum weight capacity of the knapsack
    max_weight = 10

    # Values of the items
    values = [10, 40, 50]

    # Weights of the items
    weights = [5, 4, 6]

    # Expected output: 90 (two items of weight 4 and value 40 = 80, plus one item of weight 5 and value 10)
    print("Maximum Value:", knapsack_max_value(num_items, max_weight, values, weights))

    # Visualization:
    # Knapsack capacity = 10
    # Items considered:
    #   Item 1: Value = 10, Weight = 5
    #   Item 2: Value = 40, Weight = 4
    #   Item 3: Value = 50, Weight = 6
    #
    # Optimal combination:
    #   Take 2 of Item 2 (Value = 80, Weight = 8)
    #   Take 1 of Item 1 (Value = 10, Weight = 5)
    # Total Value = 90
