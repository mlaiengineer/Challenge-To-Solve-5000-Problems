def title_case(title):
    """
    Convert a string into title case.

    Rules:
    - Capitalize the first letter of each word.
    - Make all other letters lowercase.
    - Words are separated by a single space.

    Args:
        title (str): Input string.

    Returns:
        str: Title-cased string.
    """

    # Split the string into individual words
    words = title.split()

    # List to store correctly formatted words
    formatted_words = []

    for word in words:
        # Capitalize first letter and lowercase the rest
        formatted_word = word[0].upper() + word[1:].lower()
        formatted_words.append(formatted_word)

    # Join words back into a single string with spaces
    return " ".join(formatted_words)
# Test Case 1: All uppercase input
print(title_case("JAVASCRIPT AND PYTHON"))
# Expected Output: "Javascript And Python"

# Test Case 2: Mixed case input
print(title_case("Hello world and world"))
# Expected Output: "Hello World And World"

# Test Case 3: All lowercase input
print(title_case("the quick brown fox"))
# Expected Output: "The Quick Brown Fox"

# Test Case 4: Single word
print(title_case("python"))
# Expected Output: "Python"
