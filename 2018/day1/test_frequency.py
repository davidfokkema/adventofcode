import unittest

from frequency import calculate_frequency


class FrequencyTest(unittest.TestCase):
    def test_calculate_frequency(self):
        self.assertEqual(calculate_frequency([+1, -2, +3, +1]), 3)
        self.assertEqual(calculate_frequency([+1, +1, +1]), 3)
        self.assertEqual(calculate_frequency([+1, +1, -2]), 0)
        self.assertEqual(calculate_frequency([-1, -2, -3]), -6)


if __name__ == '__main__':
    unittest.main()
