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
        cost = [10, 20, 30, 40]
        Output: 40
        Explanation:
            - Start at index 1 (cost = 20)
            - Jump two steps to index 3 (cost = 40)
            - Jump to the top (no cost)
            - Total cost = 40

        Approach:
        ---------
        This solution uses **bottom-up dynamic programming (tabulation)**:
        - We build an array `min_cost` where `min_cost[i]` represents the minimum cost
          to reach step `i`.
        - We fill this array from the base cases up to the final step.
        - The final answer is the minimum cost to reach just beyond the last step.

        Time Complexity:
        ----------------
        O(n) → We process each step once.

        Space Complexity:
        -----------------
        O(n) → We use an extra array of size `n+1` to store the DP results.

        :type cost: List[int]
        :rtype: int
        """

        length = len(cost)

        # DP array: min_cost[i] = minimum cost to reach step i
        min_cost = [0] * (length + 1)

        # Base cases: starting before step 0 or step 1 costs nothing
        min_cost[0] = 0
        min_cost[1] = 0

        # Fill DP array from step 2 to the top
        for index in range(2, length + 1):
            # Cost to reach this step from one step before
            one_step = cost[index - 1] + min_cost[index - 1]

            # Cost to reach this step from two steps before
            two_steps = cost[index - 2] + min_cost[index - 2]

            # Take the cheaper option
            min_cost[index] = min(one_step, two_steps)

        # The answer is the cost to reach beyond the last step
        return min_cost[length]


# Test the solution
if __name__ == "__main__":
    test_solution = Solution()
    cost = [10, 20, 30, 40]
    print(f"The minCostClimbingStairs({cost}) is", test_solution.minCostClimbingStairs(cost))
