# Small Python Projects

Welcome to **Small Python Projects**, a collection of 81 small, beginner-to-intermediate Python projects inspired by the *Big Book of Small Python Projects*.  

Each project is **production-ready**, with:

- Modular code (organized into packages)
- Clear docstrings and comments
- Constants and utility functions separated
- Unit tests for core logic
- Clean main entry point to run the project
- Easy-to-understand folder structure

This repository is designed to help you **practice small Python projects** with the goal of learning how to write **clean, modular, production-ready code**, so you can gradually move toward real-world Python projects.
---

## Prerequisites

Before using this repository, you should have:

- A basic understanding of **Python** (variables, loops, functions, lists/dictionaries, etc.)
- Python installed (version 3.8+ recommended)
- (Optional) Familiarity with **unit testing** using `pytest`  
---

## Repository Structure

Each project has its own folder with the following structure:

    ProjectName/
    │
    ├── projectname/          # Main package
    │   ├── __init__.py
    │   ├── game.py           # Core game logic
    │   ├── utils.py          # Helper functions
    │   └── constants.py      # Messages, hints, constants
    │
    ├── tests/                # Unit tests
    │   ├── __init__.py
    │   ├── test_game.py
    │   └── test_utils.py
    │
    ├── main.py               # Entry point
    ├── README.md             # Project-specific README
    └── requirements.txt      # Optional dependencies

---

## How to Run a Project

1. Navigate to the project folder:

        cd small-python-projects/Bagels

2. (Optional) Create a virtual environment:

        python -m venv venv
        # Linux / Mac
        source venv/bin/activate
        # Windows
        venv\Scripts\activate

3. Run the project:

        python main.py

---

## How to Run Tests

All projects have unit tests for core logic. Run them with **pytest**:

        pip install pytest          # Install pytest if not already installed
        pytest tests/

---

## Contribution Guidelines

- Each project folder is self-contained
- Follow **PEP8 style guide**
- Include **docstrings** for functions and modules
- Add **unit tests** for any new logic

---

## Author

**Thajunniza** – Sharing Python learning journey and building production-ready small projects.  
- GitHub: [https://github.com/Thajunniza/small-python-projects](https://github.com/Thajunniza/small-python-projects)  
- LinkedIn: [https://www.linkedin.com/in/thajunniza-abdullah-07745931/](https://www.linkedin.com/in/thajunniza-abdullah-07745931/)  

*Repository for 81 small Python projects from the Big Book of Small Python Projects.*