import itertools
import unittest

import spiral_memory as mem
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

    def test_generate_grid_positions(self):
        positions = list(itertools.islice(mem.generate_grid_positions(),
                                          0, 11))
        self.assertEqual(positions[0], (0, 0))
        self.assertEqual(positions[3], (0, 1))
        self.assertEqual(positions[5], (-1, 0))
        self.assertEqual(positions[9], (2, -1))

    def test_generate_memory_cells(self):
        contents = list(itertools.islice(mem.generate_memory_cells(), 0, 5))
        self.assertEqual(contents, [1, 1, 2, 4, 5])

    def test_first_memory_cell_greater_than(self):
        self.assertEqual(mem.first_memory_cell_greater_than(1), 2)
        self.assertEqual(mem.first_memory_cell_greater_than(2), 4)
        self.assertEqual(mem.first_memory_cell_greater_than(4), 5)
        self.assertEqual(mem.first_memory_cell_greater_than(747), 806)


if __name__ == '__main__':
    unittest.main()
