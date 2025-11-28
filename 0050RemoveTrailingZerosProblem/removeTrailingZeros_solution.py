class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        """
        Removes all trailing zeros from a positive integer represented as a string.

        The solution iterates backward from the end of the string to find the
        index of the first non-zero digit. The result is the substring from
        the start up to (and including) that index.

        :param num: The positive integer as a string (e.g., "51230100").
        :return: The string with trailing zeros removed (e.g., "512301").
        """
        # 1. Find the index of the last non-zero digit.
        #    We start searching from the last character (index len(num) - 1)
        #    and move toward the start of the string (index 0).
        last_non_zero_index = -1

        # We iterate backward using a counter from the end to the start (inclusive).
        # i represents the current index being checked.
        for i in range(len(num) - 1, -1, -1):
            if num[i] != '0':
                # Found the last non-zero digit.
                last_non_zero_index = i
                break

        # 2. Handle the case where the whole string is '0' (though constraints
        #    say 'num' is a positive integer, making this unlikely for string '0'
        #    unless the whole string is just a sequence of zeros '000').
        #    If no non-zero digit is found, the result is an empty string
        #    (or "0" if we strictly adhere to the 'positive integer' constraint).
        if last_non_zero_index == -1:
            # Based on the problem description, num is a positive integer,
            # so the case where all digits are '0' should not happen.
            # Returning 'num' is safer if all digits were somehow '0'
            # (e.g., "000" -> "0"). But for the constraints (positive integer),
            # a single '0' would be returned if that was the input.
            # An empty string is the technically correct result if all were removed.
            return num  # Or "" if all digits were '0'

        # 3. Slice the string from the beginning up to and including the
        #    last non-zero digit's index. Python's slice [start:end] excludes 'end',
        #    so we use last_non_zero_index + 1.
        result_string = num[:last_non_zero_index + 1]

        return result_string


# --- Demonstration/Test Cases (Outside of the class method) ---

# Variable name improvement: Use 'solver' or 'solution_instance' instead of 'test_solution'
solver = Solution()

print(f"Input: '51230100' -> Output: '{solver.removeTrailingZeros('51230100')}' (Expected: '512301')")
print(f"Input: '123' -> Output: '{solver.removeTrailingZeros('123')}' (Expected: '123')")
print(f"Input: '1000' -> Output: '{solver.removeTrailingZeros('1')}' (Expected: '1')")
print(f"Input: '10200' -> Output: '{solver.removeTrailingZeros('102')}' (Expected: '102')")
print(f"Input: '5' -> Output: '{solver.removeTrailingZeros('5')}' (Expected: '5')")