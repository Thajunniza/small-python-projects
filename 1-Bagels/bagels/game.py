import bagels.constants as const

def is_valid_number(num:str,length: int = 3) -> bool:
    """
    Check the input entered
    Args:
        num (int): Input Entered
    Returns:
        bool: Valid/Invalid Input
    """
    # Check numeric
    if not num.isdigit():
        print(const.NOT_NUMBER_ERROR)
        return False

    # Check length
    if len(num) != length:
        print(const.INVALID_LENGTH.format(length))
        return False

    # First digit should not be zero
    if num[0] == '0':
        print(const.LEADING_ZERO_ERROR)
        return False
    return True

def get_clues(guess:str,sec_num:str) -> str:
    """
    Provide the Clues based on the user input
    Args:
        guess (str) : User Input
    Returns:
        str : The Guess
    """
    clues = []
    for i,c in enumerate(guess):
        if c == sec_num[i]:
            clues.append(const.FERMI)
        elif c in sec_num:
            clues.append(const.PICO)
    if len(clues) == 0:
        return const.BAGELS
    return " ".join(clues)



    
