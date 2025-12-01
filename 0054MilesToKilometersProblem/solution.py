def convert_to_km(miles):
    """
    Convert miles to kilometers.

    Args:
        miles (float): Distance in miles (non-negative number).

    Returns:
        float: Distance converted to kilometers, rounded to two decimal places.

    Notes:
        1 mile = 1.60934 kilometers.
    """

    # Conversion factor from miles to kilometers
    KM_PER_MILE = 1.60934

    # Convert miles to kilometers
    kilometers = miles * KM_PER_MILE

    # Round the result to two decimal places
    return round(kilometers, 2)


# Example test
print(convert_to_km(3))  # Expected output: 4.83
