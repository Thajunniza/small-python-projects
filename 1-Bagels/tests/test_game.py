# tests/test_game.py

import unittest
from bagels.game import is_valid_number, get_clues
import bagels.constants as const

class TestGameLogic(unittest.TestCase):

    # -----------------------
    # Tests for is_valid_number
    # -----------------------

    def test_valid_number(self):
        self.assertTrue(is_valid_number("123", 3))

    def test_non_numeric(self):
        self.assertFalse(is_valid_number("12a", 3))

    def test_wrong_length(self):
        self.assertFalse(is_valid_number("1234", 3))

    # -----------------------
    # Tests for get_clues
    # -----------------------

    def test_all_fermi(self):
        clues = get_clues("123", "123")
        self.assertEqual(
            clues,
            f"{const.FERMI} {const.FERMI} {const.FERMI}"
        )

    def test_pico_and_fermi(self):
        clues = get_clues("132", "123")
        self.assertIn(const.FERMI, clues)
        self.assertIn(const.PICO, clues)

    def test_bagels(self):
        clues = get_clues("789", "123")
        self.assertEqual(clues, const.BAGELS)


if __name__ == "__main__":
    unittest.main()