import random
from birthday_paradox import config
from birthday_paradox import constants
from birthday_paradox import utils

def generate_birthdays(group_size: int, days_in_year: int = config.DEFAULT_DAYS_IN_YEAR) -> list[int]:
    """
    Generate a list of random birthdays for a group of people.
    It just holds a random number fro 0 - 364 which represnt 
    each day of the year
    Args:
        group_size (int): Number of people in the group.
        days_in_year (int): Number of days in a year (default: 365).

    Returns:
        list[int]: List of birthdays, each an integer from 1 to days_in_year.
    """
    birthdays = []
    for _ in range(group_size):
        birthdays.append(random.randint(0,days_in_year-1))
    return birthdays

def get_collision(birthdays: list[int]) -> dict[int,int]:
    """
    Find duplicates using sorting and two pointers.
    Returns dictionary {birthday: count}.
    """
    collision = {}
    if not birthdays:
        return collision
    birthdays.sort()
    l = 0
    i = 0
    n = len(birthdays)
    while i < n:
        count = 0
        while i < n and birthdays[i] == birthdays[l]:
            count += 1
            i += 1
        if count > 1:
            collision[birthdays[l]] = count
        l = i
    return collision

def display_collision(collision:dict[int,int]) -> str:
    """
    Display the Collision
    """
    if not collision:
        print(constants.MSG_NO_COLLISION)
        return
    n = len(collision)
    print(constants.MSG_TOTAL_COLLISIONS.format(n))
    print(f"{constants.MSG_MATCHES_HEADER}")

    for day,count in collision.items():
        bday = utils.format_bday(day)
        print(constants.MSG_MATCH_DETAIL.format(bday,count))

def run_simulations(group_size: int, simulations: int) -> float:
    """
    Run multiple birthday simulations and return probability of at least one collision.

    Args:
        group_size (int): Number of people in each group
        simulations (int): Number of simulations to run
        days_in_year (int): Number of days in a year

    Returns:
        float: Probability of at least one shared birthday (0-100)
    """
    collision_count = 0

    for i in range(simulations):
        if i % 10000 == 0:
            print(constants.MSG_SIMULATION_BREAK.format(i))
        birthdays = generate_birthdays(group_size)
        if get_collision(birthdays):
            collision_count += 1
    return collision_count


