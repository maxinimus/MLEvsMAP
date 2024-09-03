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

def validate_beta_params(a, b):
    """
    Validates the parameters of the Beta distribution.

    Parameters:
    a (float): Alpha parameter of the Beta distribution.
    b (float): Beta parameter of the Beta distribution.

    Raises:
    ValueError: If the parameters are not greater than 0.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Alpha (a) and Beta (b) parameters must be greater than 0.")
