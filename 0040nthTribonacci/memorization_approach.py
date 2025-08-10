def tribonacci(n, ht={0: 0, 1: 1, 2: 1}):
    """
    Calculates the nth Tribonacci number using top-down memoization.

    The Tribonacci sequence extends the Fibonacci concept by summing the previous 
    three terms to generate the next one:
        T(n) = T(n-1) + T(n-2) + T(n-3)

    Parameters:
    - n (int): The index of the Tribonacci number to compute.
    - ht (dict): A hash table (dictionary) storing already-computed Tribonacci values.

    Returns:
    - int: The nth Tribonacci number.

    Time Complexity:
    - O(n) — Each value of n from 0 to n is computed once and stored.

    Space Complexity:
    - O(n) — The hash table stores up to n computed values, and the call stack 
            grows up to depth n (without tail recursion optimization).
    """
    
    # ✅ Base case: If the result is already computed, return it from the hash table
    if n in ht:
        return ht[n]

    # 🧠 Recursive case: Compute and store the result for future reuse
    ht[n] = tribonacci(n - 1, ht) + tribonacci(n - 2, ht) + tribonacci(n - 3, ht)
    return ht[n]

# 🚀 Test the function
print(f"The Tribonacci of 5 is {tribonacci(5)}")  # Output: 7
