import unittest

import memory_allocation as alloc


MEMORY_CYCLES = [[0, 2, 7, 0],
                 [2, 4, 1, 2],
                 [3, 1, 2, 3],
                 [0, 2, 3, 4],
                 [1, 3, 4, 1],
                 [2, 4, 1, 2]]


class MemoryAllocationTest(unittest.TestCase):
    def test_cycle(self):
        self.assertEqual(alloc.cycle([1, 0, 0, 0]), [0, 1, 0, 0])
        self.assertEqual(alloc.cycle([0, 0, 0, 1]), [1, 0, 0, 0])
        self.assertEqual(alloc.cycle([1, 1, 0, 0]), [0, 2, 0, 0])
        self.assertEqual(alloc.cycle([3, 5, 1, 1]), [4, 1, 3, 2])

    def test_cycle_example(self):
        actual = MEMORY_CYCLES[0]
        for expected in MEMORY_CYCLES[1:]:
            actual = alloc.cycle(actual)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
