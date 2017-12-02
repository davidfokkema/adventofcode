import unittest
from unittest.mock import patch, sentinel

import evenly_divisible


class EvenlyDivisibleTest(unittest.TestCase):
    def test_find_evenly_divisible_numbers(self):
        f = evenly_divisible.find_evenly_divisible_numbers
        self.assertEqual(f([5, 9, 2, 8]), (8, 2))
        self.assertEqual(f([9, 4, 7, 3]), (9, 3))
        self.assertEqual(f([3, 8, 6, 5]), (6, 3))

    @patch.object(evenly_divisible, 'find_evenly_divisible_numbers')
    def test_divide_evenly_divisible_numbers_calls_find(self, find_func):
        # some fake numbers to make the function complete its runb
        find_func.return_value = 1, 1

        evenly_divisible.divide_evenly_divisible_numbers(sentinel.numbers)
        find_func.assert_called_once_with(sentinel.numbers)

    @patch.object(evenly_divisible, 'find_evenly_divisible_numbers')
    def test_divide_evenly_divisible_numbers_result(self, find_func):
        f = evenly_divisible.divide_evenly_divisible_numbers

        find_func.return_value = (8, 4)
        self.assertEqual(f(sentinel.numbers), 2)

        find_func.return_value = (10, 5)
        self.assertEqual(f(sentinel.numbers), 2)

        find_func.return_value = (12, 4)
        self.assertEqual(f(sentinel.numbers), 3)

    def test_calculate_checksum_result(self):
        result = evenly_divisible.calculate_checksum('test_input_part2')
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
