import unittest
from unittest.mock import patch
from birthday_paradox import simulator

class TestBirthdaySimulator(unittest.TestCase):

    def test_generate_birthdays_length(self):
        """Test that generate_birthdays returns correct number of birthdays"""
        group_size = 10
        birthdays = simulator.generate_birthdays(group_size)
        self.assertEqual(len(birthdays), group_size)
        # Each birthday should be within range 0-364
        for b in birthdays:
            self.assertTrue(0 <= b < 365)

    @patch('random.randint')
    def test_generate_birthdays_values(self, mock_randint):
        """Test that generate_birthdays produces expected mocked values"""
        mock_randint.side_effect = [0, 1, 2, 3, 4]  # deterministic
        birthdays = simulator.generate_birthdays(5)
        self.assertEqual(birthdays, [0,1,2,3,4])

    def test_get_collision_empty(self):
        """Test get_collision returns empty dict on empty list"""
        self.assertEqual(simulator.get_collision([]), {})

    def test_get_collision_no_duplicates(self):
        """Test get_collision returns empty dict if no duplicates"""
        birthdays = [1,2,3,4,5]
        self.assertEqual(simulator.get_collision(birthdays), {})

    def test_get_collision_with_duplicates(self):
        """Test get_collision detects duplicates correctly"""
        birthdays = [1,2,2,3,3,3,4]
        expected = {2:2, 3:3}
        self.assertEqual(simulator.get_collision(birthdays), expected)

    def test_run_simulations_count(self):
        """Test run_simulations counts collisions correctly with deterministic data"""
        # Mock generate_birthdays and get_collision to control outcome
        with patch('birthday_paradox.simulator.generate_birthdays') as mock_gen, \
             patch('birthday_paradox.simulator.get_collision') as mock_collision:
            mock_gen.return_value = [1,2,3]
            # Simulate collision for first two runs only
            mock_collision.side_effect = [{1:2}, {2:2}, {}, {}]
            result = simulator.run_simulations(3, 4)
            self.assertEqual(result, 2)  # only 2 runs had collisions

if __name__ == '__main__':
    unittest.main()
