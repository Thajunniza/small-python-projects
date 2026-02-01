import random
import bagels.constants as const

def generate_secret_number(length: int = 3) -> str:
    """
    Generates a random number with unique digits as a string.
    The first digit is not zero.
    Args:
        length (int): Number of digits in the secret number (default 3)
    Returns:
        str: Secret number as a string
    """
    if not isinstance(length, int):
        raise ValueError(const.INT_ERROR)
    if length < 1 or length > 10:
        raise ValueError(const.INVALID_LENGTH_MSG)
    
    # Pick first digit from 1-9 (non-zero)
    first_digit = random.randint(1, 9)
    
    # Handle single digit case
    if length == 1:
        return str(first_digit)
    
    # Pick remaining unique digits, excluding the first_digit
    remaining_digits_pool = [d for d in range(10) if d != first_digit]
    remaining_digits = random.sample(remaining_digits_pool, length - 1)
    digits = [first_digit] + remaining_digits

    return ''.join(map(str, digits))