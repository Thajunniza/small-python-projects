import unittest
from bagels.utils import generate_secret_number
import bagels.constants as const


class TestGenerateSecretNumber(unittest.TestCase):

    def test_default_length(self):
        secret = generate_secret_number()
        self.assertEqual(len(secret), 3)

    def test_custom_length(self):
        secret = generate_secret_number(5)
        self.assertEqual(len(secret), 5)

    def test_digits_only(self):
        secret = generate_secret_number(4)
        self.assertTrue(secret.isdigit())

    def test_no_leading_zero(self):
        secret = generate_secret_number(6)
        self.assertNotEqual(secret[0], "0")

    def test_unique_digits(self):
        secret = generate_secret_number(7)
        self.assertEqual(len(set(secret)), 7)

    def test_single_digit(self):
        secret = generate_secret_number(1)
        self.assertEqual(len(secret), 1)
        self.assertTrue(secret.isdigit())
        self.assertNotEqual(secret, "0")

    def test_length_zero_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            generate_secret_number(0)
        self.assertEqual(str(ctx.exception), const.INVALID_LENGTH_MSG)

    def test_length_too_large_raises_error(self):
        with self.assertRaises(ValueError):
            generate_secret_number(11)

    def test_non_int_length_raises_error(self):
        with self.assertRaises(ValueError):
            generate_secret_number("3")


if __name__ == "__main__":
    unittest.main()