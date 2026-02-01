import bagels.constants as const

def welcome_msg():
    """
    Displays the Game Welcome Message to the Player
    """
    print(const.WELCOME_MSG)
    print()
    print(const.RULES)
    print()
    print(const.CLUE)
    print()
    for clue,desc in const.CLUES_DICT.items():
        print(f"{clue} : {desc}")
    print()
    print(const.EXAMPLE)
    print()

def start_game_msg():
    print(const.YOUR_NUM)
    print()
    print(const.START_GAME)
    print()