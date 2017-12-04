import unittest

from spiral_memory import number_of_steps


class SpiralMemoryTest(unittest.TestCase):
    def test_number_of_steps(self):
        self.assertEqual(number_of_steps(1), 0)
        self.assertEqual(number_of_steps(12), 3)
        self.assertEqual(number_of_steps(23), 2)
        self.assertEqual(number_of_steps(1024), 31)


if __name__ == '__main__':
    unittest.main()
