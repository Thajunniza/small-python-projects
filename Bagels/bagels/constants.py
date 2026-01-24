"""
Constants for Bagels Game
"""
"""
Constants for Bagels Game
"""

# Welcome and Game Rules
WELCOME_MSG = """Welcome to Bagels!! A detective logic game. Are you ready to play with me?"""

RULES = """Before we start, let me explain the game and the rules.
I will think of a 3-digit number with no repeated digits.
Try to guess what it is. You will be given 10 chances.
At each chance, I will give you some clues:"""

CLUE = "When I say: That means:"

# Clues dictionary
CLUES_DICT = {
    "PICO": "One digit in your guess is correct but in the wrong position",
    "FERMI": "One digit and its position in your guess is correct",
    "BAGELS": "No digit is correct"
}

EXAMPLE = """For example, if the secret number was 248 and your guess was 843,
then the clues would be: Fermi Pico."""

# Hint keywords
FERMI = "Fermi"
PICO = "Pico"
BAGELS = "Bagels"

# Start the Game
YOUR_NUM = "I am ready.. I have a Magic number for you."
START_GAME= "Start your guess.."

# Messages
CONGRATS_MSG = "Congratulations! You guessed the number! Bravo !!!"
INVALID_LENGTH_MSG = "Length must be an integer between 1 and 10."
INT_ERROR = "Input must be an integer"
GUESS_PROMPT = "Guess #{}:"
MAX_GUESS = "You have {} guesses to find my Magic number"
NOT_NUMBER_ERROR = "Please enter a valid number."
INVALID_LENGTH = "Number must be exactly {} digits long."
LEADING_ZERO_ERROR = "Number cannot start with zero."



