# Birthday Paradox – Probability Simulation

**Birthday Paradox** is a simulation that demonstrates how likely it is for **two people in a group to share the same birthday**. The player can generate birthdays, check for collisions, and run multiple simulations to estimate probabilities. This project is designed to demonstrate **production-ready Python code** with modular design, utility functions, constants, and unit tests.

## Prerequisites

- Basic knowledge of Python (variables, loops, functions, lists/dictionaries)  
- Python 3.8+ installed  
- Optional: familiarity with **unittest** for running unit tests

## Project Structure

Birthday-Paradox/
├── birthday_paradox/  
│   ├── __init__.py  
│   ├── simulator.py  
│   ├── utils.py  
│   ├── constants.py  
│   └── config.py  
├── tests/  
│   ├── __init__.py  
│   ├── test_simulator.py  
│   └── test_utils.py  
├── examples/  
│   └── run_simulation.py  
├── main.py  
├── run.py.py  
└── README.md  

## How to Run

1. Navigate to the project folder:  
`cd small-python-projects/2-Birthday-Paradox`

2. Run the interactive game:  
`python run.py`

3. Menu options:  
   - **1** → Play Birthday Paradox (generate birthdays, see collisions, run simulation)  
   - **2** → Run all unit tests  
   - **3** → Exit  

4. Run unit tests directly:  
`python -m unittest discover -s tests -p "*.py"`

## How to Play

1. Enter the number of people in the group when prompted.  
2. The program generates random birthdays for the group.  
3. It checks for collisions and displays any shared birthdays.  
4. Optionally, run multiple simulations to estimate the probability of shared birthdays in that group size.  
5. Review the simulation results and probability summary.

## Key Learnings

1. **Random Birthday Generation:** Used Python's `random` library to generate birthdays for a group.  
2. **Collision Detection:** Implemented a **sorted two-pointer algorithm** to efficiently find duplicate birthdays.  
3. **Simulation & Probability:** Ran multiple simulations to calculate the probability of shared birthdays.  
4. **Modular Programming:** Code separated into modules (`simulator`, `utils`, `constants`, `config`) for clarity and testability.  
5. **Unit Testing:** Validated collision detection, birthday formatting, and input handling using `unittest`.  
6. **Constants & Formatting:** Centralized messages in `constants.py` for easy customization.  
7. **Python Best Practices:** Applied `if __name__ == "__main__":`, input validation, and separation of concerns.

## Author

**Thajunniza** – Sharing Python learning journey and building production-ready small projects  

- GitHub: [https://github.com/Thajunniza/small-python-projects](https://github.com/Thajunniza/small-python-projects)  
- LinkedIn: [https://www.linkedin.com/in/thajunniza-abdullah-07745931/](https://www.linkedin.com/in/thajunniza-abdullah-07745931/)
