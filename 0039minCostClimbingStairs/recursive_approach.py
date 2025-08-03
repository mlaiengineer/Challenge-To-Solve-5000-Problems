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
        cost = [10, 15, 20]
        Output: 15
        Explanation:
            - Start at index 1 (cost = 15), then jump two steps to the top.
            - Total cost = 15

        Time Complexity:
        ----------------
        O(2^n) → At each step, you explore two possibilities (1 step or 2 steps).
        This creates an exponential growth in recursive calls.

        Space Complexity:
        -----------------
        O(n) → The maximum depth of the recursion tree is `n` (number of steps).
        This space is used in the call stack.

        """

        # Helper function to compute the minimum cost starting from a given index
        def costFrom(index):
            # Base case: If we go beyond the last step, no cost is added
            if index >= len(cost):
                return 0

            # Current step cost
            current_step = cost[index]

            # Option 1: Take one step and pay the cost
            cost_if_one_step = current_step + costFrom(index + 1)

            # Option 2: Take two steps and pay the cost
            cost_if_two_steps = current_step + costFrom(index + 2)

            # Return the cheaper option
            return min(cost_if_one_step, cost_if_two_steps)

        # We can start at step 0 or step 1, so take the cheaper starting point
        return min(costFrom(0), costFrom(1))


if __name__ == "__main__":
    test_solution = Solution()
    cost = [10, 15, 20]
    print(f"The minCostClimbingStairs({cost}) is", test_solution.minCostClimbingStairs(cost))
