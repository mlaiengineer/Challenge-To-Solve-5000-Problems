def tabulationKnapsack(max_weight, weights, values, num_items):
    """
    Problem:
    Solve the 0/1 Knapsack Problem using the tabulation (bottom-up dynamic programming) approach.
    The goal is to maximize the total value of items in the knapsack without exceeding its weight capacity.

    Inputs:
        - max_weight (int): The maximum weight capacity of the knapsack.
        - weights (list[int]): A list of weights for each item.
        - values (list[int]): A list of values for each item.
        - num_items (int): The number of items available.

    Output:
        - int: The maximum value that can be achieved without exceeding the weight limit.

    Example:
        Input:
            max_weight = 8
            weights = [1, 3, 4, 5]
            values = [1, 4, 5, 7]
            num_items = 4
        Output:
            9
        Explanation:
            The optimal solution includes the second and fourth items with weights 3 and 5, 
            and values 4 and 7, respectively, for a total value of 9.

    Time Complexity:
        - O(num_items * max_weight): We iterate through all items and all weight capacities.

    Space Complexity:
        - O(num_items * max_weight): Space used by the DP table.
    """

    # Base case: If there are no items or the weight capacity is zero
    if max_weight == 0 or num_items == 0:
        return 0

    # Initialize the DP table with 0s
    dp_table = [[0] * (max_weight + 1) for _ in range(num_items + 1)]

    # Fill the DP table iteratively
    for i in range(1, num_items + 1):  # Iterate through items
        for j in range(1, max_weight + 1):  # Iterate through weight capacities
            # Case 1: Exclude the current item
            exclude_item = dp_table[i - 1][j]

            # Case 2: Include the current item (if weight allows)
            include_item = 0
            if weights[i - 1] <= j:
                include_item = values[i - 1] + dp_table[i - 1][j - weights[i - 1]]

            # Take the maximum of including or excluding the item
            dp_table[i][j] = max(include_item, exclude_item)

    # Return the maximum value for the full weight capacity and all items
    return dp_table[num_items][max_weight]


# Test Cases
if __name__ == "__main__":
    # Example 1
    max_weight = 8
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    num_items = len(weights)
    print("Maximum value:", tabulationKnapsack(max_weight, weights, values, num_items))  # Output: 9

    # Example 2
    max_weight = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    num_items = len(weights)
    print("Maximum value:", tabulationKnapsack(max_weight, weights, values, num_items))  # Output: 220

    # Example 3
    max_weight = 4
    weights = [4, 2, 3]
    values = [10, 4, 7]
    num_items = len(weights)
    print("Maximum value:", tabulationKnapsack(max_weight, weights, values, num_items))  # Output: 10
