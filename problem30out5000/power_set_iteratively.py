def power_set(array, debug=False):
    """
    Generate the power set (all subsets) of a given list iteratively.

    Args:
        array (list): The input list of elements.
        debug (bool): If True, prints intermediate steps of power set construction.

    Returns:
        list: A list of lists representing all possible subsets of the input list.
    """
    result = [[]]  # Start with the empty subset

    for current_element in array:
        new_subsets = []

        for subset in result:
            # Create a new subset by adding the current element to the existing subset
            new_subset = subset + [current_element]
            new_subsets.append(new_subset)

        # Add the new subsets to the result
        result.extend(new_subsets)

        # Optional debug print to trace the steps
        if debug:
            print(f"After adding {current_element}, power set becomes: {result}")

    return result


# Example usage
if __name__ == "__main__":
    sample_input = [1, 2]
    power_set_result = power_set(sample_input, debug=True)
    print("Final Power Set:", power_set_result)
