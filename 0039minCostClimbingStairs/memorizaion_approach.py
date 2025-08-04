class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        Problem:
        --------
        You are given an integer array `cost` where `cost[i]` represents the cost of step `i`.
        Once you pay the cost for a step, you can climb either:
            - One step, or
            - Two steps
        You can start at step 0 or step 1.
        Your goal is to reach the top of the staircase with the minimum cost.

        Example:
        --------
        cost = [10, 15, 20, 25]
        Output: 30
        Explanation:
            - Start at index 0 (cost = 10)
            - Take one step to index 2 (cost = 20)
            - Reach the top (no additional cost)
            - Total cost = 10 + 20 = 30

        Approach:
        ---------
        This solution uses **top-down recursion with memoization**:
        - We recursively compute the cost of starting from each step.
        - We store already-computed results in a memoization array (`min_cost`)
          to avoid recalculating them.
        - We return the cheaper option between starting at step 0 and step 1.

        Time Complexity:
        ----------------
        O(n) → Each step is computed only once due to memoization.

        Space Complexity:
        -----------------
        O(n) → Space is used for the `min_cost` array and recursion call stack.

        :type cost: List[int]
        :rtype: int
        """

        # Memoization array to store computed minimum costs for each step
        min_cost = [-1] * len(cost)

        # Helper function to compute the minimum cost starting from a given step
        def costFrom(index):
            # Base case: If beyond the last step, no cost is added
            if index >= len(cost):
                return 0

            # If already computed, return stored value (avoid recalculation)
            if min_cost[index] != -1:
                return min_cost[index]

            # Option 1: Take one step forward
            cost_if_one_step = cost[index] + costFrom(index + 1)

            # Option 2: Take two steps forward
            cost_if_two_steps = cost[index] + costFrom(index + 2)

            # Store the cheaper option in memoization array
            min_cost[index] = min(cost_if_one_step, cost_if_two_steps)

            return min_cost[index]

        # Try starting from step 0 or step 1, return the cheaper option
        return min(costFrom(0), costFrom(1))


if __name__ == "__main__":
    test_solution = Solution()
    cost = [10, 15, 20, 25]
    print(f"The minCostClimbingStairs({cost}) is", test_solution.minCostClimbingStairs(cost))
