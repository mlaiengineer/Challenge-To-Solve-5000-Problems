def tribonacci(n: int) -> int:
    """
    Compute the n-th Tribonacci number using bottom-up tabulation.

    Recurrence:
        For n >= 3,  T(n) = T(n-1) + T(n-2) + T(n-3)
        Base cases:  T(0) = 0, T(1) = 1, T(2) = 1

    Parameters:
    - n (int): Index of the Tribonacci number (n >= 0).

    Returns:
    - int: The n-th Tribonacci number.

    Time Complexity:
    - O(n) — Single pass from 3 to n.

    Space Complexity:
    - O(n) — Stores all values up to n (can be reduced to O(1) with a rolling window).
    """
    # Input validation (helps catch silent bugs)
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    # Base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Bottom-up table fill
    dp_table = [0] * (n + 1)
    dp_table[0], dp_table[1], dp_table[2] = 0, 1, 1

    for index in range(3, n + 1):
        dp_table[index] = (
            dp_table[index - 1] +
            dp_table[index - 2] +
            dp_table[index - 3]
        )

    return dp_table[n]
#test the solution
assert tribonacci(0) == 0
assert tribonacci(1) == 1
assert tribonacci(2) == 1
assert tribonacci(3) == 2
assert tribonacci(4) == 4
assert tribonacci(5) == 7
assert tribonacci(6) == 13

print("All tabulation tests passed.")
