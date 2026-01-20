from typing import List


class Solution:
    def final_value_after_operations(self, operations: List[str]) -> int:
        """
        Computes the final value of variable X after performing all operations.

        Each operation is one of:
        "++X", "X++" → increment
        "--X", "X--" → decrement

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        value = 0

        for op in operations:
            # If operation contains '++' → increment, otherwise decrement
            if "++" in op:
                value += 1
            else:
                value -= 1

        return value
