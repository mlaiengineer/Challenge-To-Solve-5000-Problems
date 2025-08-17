def knapsack(max_weight, num_items, values, weights):
    """
    Problem:
    The Knapsack Problem involves selecting a subset of items to maximize their total value 
    while staying within a given weight capacity (max_weight). Each item has a specific weight 
    and value, and you can either include the item in the knapsack or exclude it. Using memoization, 
    we optimize the solution to avoid redundant calculations.

    Inputs:
        - max_weight (int): The maximum weight capacity of the knapsack.
        - num_items (int): The total number of items available.
        - values (list[int]): A list of values for each item.
        - weights (list[int]): A list of weights for each item.

    Output:
        - int: The maximum value achievable without exceeding the weight limit.

    Example:
        Input:
            max_weight = 3
            num_items = 3
            values = [1, 2, 3]
            weights = [2, 1, 3]
        Output:
            3
        Explanation:
            The optimal solution includes the third item with weight 3 and value 3, 
            for a total value of 3.

    Time Complexity:
        - O(num_items * max_weight): Each state is computed once and stored in the DP table.

    Space Complexity:
        - O(num_items * max_weight): Space used by the DP table.
    """

    # Initialize a DP table with -1 (indicating uncomputed states)
    dp_table = [[-1] * (max_weight + 1) for _ in range(num_items)]

    def solveKnapsack(index, remaining_weight):
        """
        Recursive helper function to solve the knapsack problem with memoization.

        Args:
            index (int): The current item index being considered.
            remaining_weight (int): The remaining weight capacity of the knapsack.

        Returns:
            int: The maximum value achievable from the current state.
        """
        # Base Case: If all items have been considered or weight capacity is zero
        if index >= num_items or remaining_weight == 0:
            return 0 #means we can't add furher items

        # If the result for this state is already computed, return it
        if dp_table[index][remaining_weight] != -1:
            return dp_table[index][remaining_weight]

        # Case 1: Exclude the current item
        exclude_item = solveKnapsack(index + 1, remaining_weight)

        # Case 2: Include the current item (if weight allows)
        include_item = 0
        if weights[index] <= remaining_weight:
            include_item = values[index] + solveKnapsack(index + 1, remaining_weight - weights[index])

        # Store the result in the DP table and return it
        dp_table[index][remaining_weight] = max(include_item, exclude_item)
        return dp_table[index][remaining_weight]

    # Start solving from the first item with the full weight capacity
    return solveKnapsack(0, max_weight)


# Test Cases
if __name__ == "__main__":
    # Example 1
    max_weight = 3
    num_items = 3
    values = [1, 2, 3]
    weights = [2, 1, 3]
    print("Maximum value:", knapsack(max_weight, num_items, values, weights))  # Output: 3

    # Example 2
    max_weight = 8
    num_items = 4
    values = [1, 4, 5, 7]
    weights = [1, 3, 4, 5]
    print("Maximum value:", knapsack(max_weight, num_items, values, weights))  # Output: 9
