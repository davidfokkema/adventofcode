import itertools
import unittest

from spiral_memory import (number_of_steps, manhattan_distance,
                           get_coordinates_for_square, generate_spiral_steps)


class SpiralMemoryTest(unittest.TestCase):
    def test_number_of_steps(self):
        self.assertEqual(number_of_steps(1), 0)
        self.assertEqual(number_of_steps(12), 3)
        self.assertEqual(number_of_steps(23), 2)
        self.assertEqual(number_of_steps(1024), 31)

    def test_manhattan_distance(self):
        self.assertEqual(manhattan_distance(0, 0), 0)
        self.assertEqual(manhattan_distance(2, 1), 3)
        self.assertEqual(manhattan_distance(0, -2), 2)

    def test_get_coordinates_for_square(self):
        self.assertEqual(get_coordinates_for_square(1), (0, 0))
        self.assertEqual(get_coordinates_for_square(12), (2, 1))
        self.assertEqual(get_coordinates_for_square(23), (0, -2))

    def test_generate_spiral_steps(self):
        steps = list(itertools.islice(generate_spiral_steps(), 0, 10))
        self.assertEqual(steps, ['RIGHT'] + ['UP'] + 2 * ['LEFT'] +
                         2 * ['DOWN'] + 3 * ['RIGHT'] + ['UP'])


if __name__ == '__main__':
    unittest.main()
