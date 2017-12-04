import unittest

from spiral_memory import number_of_steps, manhattan_distance


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


if __name__ == '__main__':
    unittest.main()
