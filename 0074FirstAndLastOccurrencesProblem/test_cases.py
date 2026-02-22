from problem_solution import Solution

test = Solution()

# --- Original Test Case ---

# Test: x appears multiple times at the beginning
assert test.find([1, 1, 2], 1) == [0, 1]

# --- Core Functionality Tests ---

# Test: x appears multiple times in the middle of the array
assert test.find([1, 3, 5, 5, 5, 5, 67, 123, 125], 5) == [2, 5]

# Test: x appears only once in the array
assert test.find([1, 3, 5, 5, 5, 5, 7, 123, 125], 7) == [6, 6]

# Test: x does not exist in the array
assert test.find([1, 2, 3], 4) == [-1, -1]

# --- Edge Cases ---

# Test: array has only one element and it matches x
assert test.find([5], 5) == [0, 0]

# Test: array has only one element and it doesn't match x
assert test.find([5], 3) == [-1, -1]

# Test: all elements in the array are equal to x
assert test.find([7, 7, 7, 7, 7], 7) == [0, 4]

# Test: x is the first element only
assert test.find([1, 2, 3, 4, 5], 1) == [0, 0]

# Test: x is the last element only
assert test.find([1, 2, 3, 4, 5], 5) == [4, 4]

# Test: large array with x at boundaries
assert test.find([2] + [5] * 999998 + [9], 5) == [1, 999998]

# Test: x is smaller than all elements in the array
assert test.find([3, 5, 7, 9, 11], 1) == [-1, -1]

# Test: x is larger than all elements in the array
assert test.find([1, 2, 3, 4, 5], 100) == [-1, -1]

# Test: array with two elements both matching x
assert test.find([4, 4], 4) == [0, 1]

# Test: array with two elements none matching x
assert test.find([4, 6], 5) == [-1, -1]

print("Passed all test cases! ✅")