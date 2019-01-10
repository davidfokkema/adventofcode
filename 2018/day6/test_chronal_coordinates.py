import unittest

import numpy as np

from chronal_coordinates import (find_largest_area,
                                 calculate_manhattan_distances,
                                 find_closest_coordinate, get_letter)


TEST_COORDS = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]


class ChronalCoordinateTest(unittest.TestCase):
    def test_find_largest_area(self):
        self.assertEqual(find_largest_area(TEST_COORDS), 17)

    def test_calculate_manhattan_distances(self):
        coordinates = [(4, 2), (8, 7)]
        position = (3, 2)

        distances = calculate_manhattan_distances(position, coordinates)
        np.testing.assert_equal(distances, np.array([1, 10]))

    def test_more_calculate_manhattan_distances(self):
        coordinates = [(3, 4), (1, 6)]
        position = (3, 6)

        distances = calculate_manhattan_distances(position, coordinates)
        np.testing.assert_equal(distances, np.array([2, 2]))

    def test_find_closest_coordinate(self):
        self.assertEqual(find_closest_coordinate((0, 0), TEST_COORDS), 1)
        self.assertEqual(find_closest_coordinate((6, 1), TEST_COORDS), 3)
        self.assertEqual(find_closest_coordinate((1, 1), TEST_COORDS), -1)
        self.assertEqual(find_closest_coordinate((1, 4), TEST_COORDS), 0)
        self.assertEqual(find_closest_coordinate((1, 6), TEST_COORDS), -2)
        self.assertEqual(find_closest_coordinate((2, 6), TEST_COORDS), 2)
        self.assertEqual(find_closest_coordinate((3, 6), TEST_COORDS), 0)

    def test_get_letter(self):
        self.assertEqual(get_letter(-2), 'B')
        self.assertEqual(get_letter(2), 'b')
        self.assertEqual(get_letter(0), '.')


if __name__ == '__main__':
    unittest.main()
