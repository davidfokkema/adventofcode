import unittest
from unittest.mock import patch, mock_open

from frequency import FrequencyShifter, read_shifts_from_file


class FrequencyTest(unittest.TestCase):
    def setUp(self):
        self.shifter = FrequencyShifter(0)

    def test_calculate_frequency(self):
        self.assertEqual(self.shifter.calculate_frequency([+1, -2, +3, +1]), 3)
        self.assertEqual(self.shifter.calculate_frequency([+1, +1, +1]), 3)
        self.assertEqual(self.shifter.calculate_frequency([+1, +1, -2]), 0)
        self.assertEqual(self.shifter.calculate_frequency([-1, -2, -3]), -6)

    def test_read_shifts_from_file(self):
        mock = mock_open(read_data="-1\n-2\n+3\n")
        with patch('frequency.open', mock):
            shifts = read_shifts_from_file('foo.txt')
        self.assertEqual(shifts, [-1, -2, 3])

    def test_has_duplicates(self):
        self.shifter.frequencies = [1, 2, 3]
        self.assertEqual(self.shifter.has_duplicates(), False)
        self.shifter.frequencies = [1, 2, 3, 2]
        self.assertEqual(self.shifter.has_duplicates(), True)

    def test_find_first_duplicate_frequency(self):
        self.assertEqual(self.shifter.find_first_duplicate_frequency([+1, -1]), 0)
        self.assertEqual(self.shifter.find_first_duplicate_frequency([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(self.shifter.find_first_duplicate_frequency([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(self.shifter.find_first_duplicate_frequency([+7, +7, -2, -7, -4]), 14)


if __name__ == '__main__':
    unittest.main()
