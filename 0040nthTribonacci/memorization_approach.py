def tribonacci(n, ht={0: 0, 1: 1, 2: 1}):
    """
    Calculates the nth Tribonacci number using top-down memoization.

    Parameters:
    - n (int): The index of the Tribonacci number to compute.
    - ht (dict): A hash table (dictionary) storing already-computed Tribonacci values.

    Returns:
    - int: The nth Tribonacci number.
    """

    # ✅ Base case: If the result is already computed, return it from the hash table
    if n in ht:
        return ht[n]

    # 🧠 Recursive case: Compute and store the result for future reuse
    ht[n] = tribonacci(n - 1, ht) + tribonacci(n - 2, ht) + tribonacci(n - 3, ht)
    return ht[n]

# 🚀 Test the function
print(f"The Tribonacci of 5 is {tribonacci(5)}")  # Output: 7
