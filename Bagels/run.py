# run.py
from main import main as run_game
import unittest

def run_tests():
    print("Running all unit tests...")
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main_menu():
    while True:
        print("\n=== Bagels Runner ===")
        print("1. Play Bagels Game")
        print("2. Run Unit Tests")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            run_game()
        elif choice == "2":
            run_tests()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()