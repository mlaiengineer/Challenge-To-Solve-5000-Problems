def vowel_case(s: str) -> str:
    """
    Converts all vowels in the input string to uppercase and all
    non-vowel characters to lowercase.

    Parameters:
        s (str): The input string.

    Returns:
        str: A new string where vowels are uppercase and other
             characters are lowercase.

    Time Complexity:
        O(n) - where n is the length of the input string. Each character
               is processed once.

    Space Complexity:
        O(n) - A new string is created with the same length as the input.
    """
    # Initialize the result string
    vowel_case_s = ''

    # Iterate through each character in the string (converted to lowercase)
    for char in s.lower():
        # If the character is a vowel, convert it to uppercase
        if char in 'aeiou':
            vowel_case_s += char.upper()
        else:
            # Otherwise, keep it as lowercase
            vowel_case_s += char.lower()

    return vowel_case_s


# Test Cases
def test_vowel_case():
    """
    Test the vowel_case function with various input strings to verify correctness.
    """
    # Test with a mix of vowels and consonants
    assert vowel_case('vowelcase') == 'vOwElcAsE', "Test Case 1 Failed"

    # Test with spaces and lowercase letters
    assert vowel_case('coding is fun') == 'cOdIng Is fUn', "Test Case 2 Failed"

    # Test with uppercase input and punctuation
    assert vowel_case('HELLO, world!') == 'hEllO, wOrld!', "Test Case 3 Failed"

    # Test with an empty string
    assert vowel_case('') == '', "Test Case 4 Failed"

    # Test with only vowels
    assert vowel_case('aeiou') == 'AEIOU', "Test Case 5 Failed"

    # Test with only consonants
    assert vowel_case('bcdfg') == 'bcdfg', "Test Case 6 Failed"

    # Test with mixed case and numbers
    assert vowel_case('Python3.9') == 'pythOn3.9', "Test Case 7 Failed"

    print("All test cases passed!")


# Run the tests
test_vowel_case()