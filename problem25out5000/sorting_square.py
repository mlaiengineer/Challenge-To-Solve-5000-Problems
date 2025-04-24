"""
Question:
You are given an array of integers in which each subsequent value is not less than the previous value. Write a function 
that takes this array as input and returns a new array with the squares of each number sorted in ascending order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [9,9,49,49,121]
Explanation: After squaring, the array becomes [49,9,4,9,121]. After sorting, it becomes [9,9,49,49,121].

"""

def square_sort_asc(arr: list):
    """
    This function takes an array of integers and returns a new array with the squares of each number, sorted in ascending order.
    
    Time Complexity:
    - The time complexity is O(n log n) due to the sorting step after squaring.
    
    Space Complexity:
    - The space complexity is O(n) for storing the squared values in the new array.
    
    Parameters:
    - arr (list): The input list of integers.
    
    Returns:
    - list: The array of squared numbers sorted in ascending order.
    """
    # If the array is empty, return an empty array
    if len(arr) == 0:
        return arr
    
    # Initialize an empty array to store squared values
    new_arr = []
    for num in arr:
        new_arr.append(num * num)  # Square each number and add it to the new array

    new_arr.sort()  # Sort the array in ascending order
    
    return new_arr


# Test Cases
print(square_sort_asc([]))  # Test with an empty array, should return []
print(square_sort_asc([1, 2, 3]))  # Test with a sorted array, should return [1, 4, 9]
print(square_sort_asc([5, -3, -7, 2]))  # Test with both negative and positive numbers, should return [4, 9, 25, 49]
print(square_sort_asc([-7, -3, 2, 3, 11]))  # Test with both negative and positive numbers, should return [9, 9, 49, 49, 121]
