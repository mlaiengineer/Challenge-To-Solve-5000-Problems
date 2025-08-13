def knapSack(W, weights, values, n):
    """
    Problem:
    The Knapsack Problem involves selecting a subset of items to maximize their total value 
    while staying within a given weight capacity (W). Each item has a specific weight and value, 
    and you can either include the item in the knapsack or exclude it. This is a classic 
    optimization problem in computer science.

    Inputs:
        - W (int): The maximum weight capacity of the knapsack.
        - weights (list[int]): A list of weights for each item.
        - values (list[int]): A list of values for each item.
        - n (int): The number of items available.

    Output:
        - int: The maximum value that can be achieved without exceeding the weight limit.

    Example:
        Input:
            W = 8
            weights = [8, 2, 5]
            values = [2, 3, 9]
            n = 3
        Output:
            12
        Explanation:
            The optimal solution includes the second and third items with weights 2 and 5, and 
            values 3 and 9, respectively, for a total value of 12.

    Time Complexity:
        - O(2^n): In the worst case, we explore all subsets of items (include or exclude each item).

    Space Complexity:
        - O(n): The space is used for the recursion stack (maximum depth is `n`).

    Approach:
    This is solved using recursion by considering two cases for each item:
        1. Exclude the item and move to the next.
        2. Include the item (if its weight allows) and subtract its weight from the remaining capacity.
    """

    def recursiveKnapSack(index, remaining_weight):
        """
        Helper function to solve the knapsack problem recursively.

        Args:
            index (int): The current item index being considered.
            remaining_weight (int): The remaining weight capacity of the knapsack.

        Returns:
            int: The maximum value achievable from the current state.
        """
        # Base Case: If we've considered all items or the remaining weight is 0
        if index >= n or remaining_weight == 0:
            return 0

        # Case 1: Exclude the current item
        exclude = recursiveKnapSack(index + 1, remaining_weight)

        # Case 2: Include the current item (if weight allows)
        include = 0
        if weights[index] <= remaining_weight:
            include = values[index] + recursiveKnapSack(index + 1, remaining_weight - weights[index])

        # Return the maximum value from including or excluding the item
        return max(include, exclude)

    # Start the recursion from the first item with the full weight capacity
    return recursiveKnapSack(0, W)


# Test Case
if __name__ == "__main__":
    W = 8
    weights = [8, 2, 5]
    values = [2, 3, 9]
    n = len(weights)
    print("Maximum value:", knapSack(W, weights, values, n))
