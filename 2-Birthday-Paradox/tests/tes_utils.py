import unittest
from birthday_paradox import utils, config

class TestUtils(unittest.TestCase):

    def test_format_bday_first_day(self):
        """Test formatting for the first day of the year"""
        self.assertEqual(utils.format_bday(1), "Jan 01")

    def test_format_bday_middle_of_year(self):
        """Test formatting for a middle day of the year"""
        # 32nd day = Feb 01
        self.assertEqual(utils.format_bday(32), "Feb 01")

    def test_format_bday_end_of_year(self):
        """Test formatting for the last day of the year"""
        # 365th day = Dec 31
        self.assertEqual(utils.format_bday(365), "Dec 31")

    def test_validate_group_size_valid(self):
        """Test valid group size"""
        self.assertTrue(utils.validate_group_size("1", max_size=50))
        self.assertTrue(utils.validate_group_size("25", max_size=50))
        self.assertTrue(utils.validate_group_size("50", max_size=50))

    def test_validate_group_size_invalid(self):
        """Test invalid group sizes"""
        self.assertFalse(utils.validate_group_size("0", max_size=50))
        self.assertFalse(utils.validate_group_size("51", max_size=50))
        self.assertFalse(utils.validate_group_size("-5", max_size=50))
        self.assertFalse(utils.validate_group_size("abc", max_size=50))
        self.assertFalse(utils.validate_group_size("", max_size=50))


if __name__ == "__main__":
    unittest.main()
