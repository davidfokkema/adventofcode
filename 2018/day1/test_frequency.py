import unittest
from unittest.mock import patch, mock_open

from frequency import (calculate_frequency, read_shifts_from_file,
                        has_duplicates, find_first_duplicate_frequency)


class FrequencyTest(unittest.TestCase):
    def test_calculate_frequency(self):
        self.assertEqual(calculate_frequency([+1, -2, +3, +1]), 3)
        self.assertEqual(calculate_frequency([+1, +1, +1]), 3)
        self.assertEqual(calculate_frequency([+1, +1, -2]), 0)
        self.assertEqual(calculate_frequency([-1, -2, -3]), -6)

    def test_read_shifts_from_file(self):
        mock = mock_open(read_data="-1\n-2\n+3\n")
        with patch('frequency.open', mock):
            shifts = read_shifts_from_file('foo.txt')
        self.assertEqual(shifts, [-1, -2, 3])

    def test_has_duplicates(self):
        self.assertEqual(has_duplicates([1, 2, 3]), False)
        self.assertEqual(has_duplicates([1, 2, 3, 2]), True)

    def test_find_first_duplicate_frequency(self):
        self.assertEqual(find_first_duplicate_frequency([+1, -1]), 0)
        self.assertEqual(find_first_duplicate_frequency([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(find_first_duplicate_frequency([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(find_first_duplicate_frequency([+7, +7, -2, -7, -4]), 14)


if __name__ == '__main__':
    unittest.main()
