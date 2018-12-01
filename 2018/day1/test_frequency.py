import unittest
from unittest.mock import patch, mock_open

from frequency import calculate_frequency, read_shifts_from_file


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


if __name__ == '__main__':
    unittest.main()
