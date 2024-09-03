def validate_coin_tosses(n, h):
    """
    Validates the number of coin tosses and heads.

    Parameters:
    n (int): Number of coin tosses.
    h (int): Number of heads.

    Raises:
    ValueError: If the number of tosses is less than 1 or the number of heads is not in the correct range.
    """
    if n < 1:
        raise ValueError("Number of coin tosses must be greater than 0.")
    if h < 0 or h > n:
        raise ValueError("Number of heads must be between 0 and the number of coin tosses.")

