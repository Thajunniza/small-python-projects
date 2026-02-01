# Bagels/main.py

import bagels.utils as utils
import bagels.display as display
import bagels.constants as const
import bagels.game as game

def main():
    max_guess = 10
    default_digit = 3
    #show welcome message
    display.welcome_msg()

    # get the secret number
    sec_num = utils.generate_secret_number(default_digit)
    display.start_game_msg()
    print(const.MAX_GUESS.format(max_guess))
    for attempt in range(1,max_guess+1):
        while True:
            guess = input(const.GUESS_PROMPT.format(attempt)) # Inserts attempt number
            if game.is_valid_number(guess,default_digit):
                break
        
        if guess == sec_num:
            print(const.CONGRATS_MSG)
            break
        clues = game.get_clues(guess,sec_num)
        print(clues)
        
                


    

if __name__ == "__main__":
    main()