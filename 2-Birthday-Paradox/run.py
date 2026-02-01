from main import main as run_game
import unittest

def run_tests():
    print("\n=== Running all Birthday Paradox unit tests ===\n")
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def main_menu():
    while True:
        print("\n=== Birthday Paradox Runner ===")
        print("1. Play Birthday Paradox Game")
        print("2. Run Unit Tests")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            run_game()
        elif choice == "2":
            run_tests()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
