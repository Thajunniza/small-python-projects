import datetime
from birthday_paradox import config

def format_bday(day_number: int) -> str:
    """
    Format the int day to Month Date
    eg 1 to Jan 2
    
    :param day_number: Day Number
    :type day_number: int
    :return: Formatted Date
    :rtype: str
    """
    # We will consider 2001 which is the non -leap year
    start_date = datetime.date(2001,1,1)
    bday_date = start_date + datetime.timedelta(days = day_number-1)
    return bday_date.strftime("%b %d")

def validate_group_size(usr_input:str, max_size:int = config.MAX_GROUP_SIZE) -> bool:
    """
    Validate if the input string is an integer between 1 and max_size.

    Args:
        input_str (str): User input string.
        max_size (int): Maximum allowed group size.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        val = int(usr_input)
        if 1 <= val <= max_size:
            return True 
        return False
    except ValueError:
        return False
