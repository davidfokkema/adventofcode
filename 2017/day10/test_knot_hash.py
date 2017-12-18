import unittest

from knot_hash import Ring


class RingTest(unittest.TestCase):
    def setUp(self):
        self.ring = Ring(range(5))

    def test_ring_has_attribute_ring(self):
        self.assertTrue(hasattr(self.ring, '_ring'))

    def test_ring_attribute_is_init_list(self):
        self.assertEqual(self.ring._ring, [0, 1, 2, 3, 4])

    def test_get_ring_element(self):
        self.assertEqual(self.ring[0], 0)
        self.assertEqual(self.ring[2], 2)
        self.assertEqual(self.ring[4], 4)

    def test_ring_loops_around(self):
        self.assertEqual(self.ring[5], 0)
        self.assertEqual(self.ring[7], 2)
        self.assertEqual(self.ring[20], 0)

    def test_negative_indexing(self):
        self.assertEqual(self.ring[-1], 4)
        self.assertEqual(self.ring[-3], 2)

    def test_negative_indexing_loops_around(self):
        self.assertEqual(self.ring[-6], 4)
        self.assertEqual(self.ring[-21], 4)
        self.assertEqual(self.ring[-22], 3)

    def test_simple_slicing(self):
        self.assertEqual(self.ring[1:3], [1, 2])

    def test_simple_step(self):
        self.assertEqual(self.ring[0:5:2], [0, 2, 4])

    def test_reverse_slicing(self):
        self.assertEqual(self.ring[3:0:-1], [3, 2, 1])

    def test_slicing_loops_both_ways(self):
        self.assertEqual(self.ring[3:7], [3, 4, 0, 1])
        self.assertEqual(self.ring[6:2:-1], [1, 0, 4, 3])

    def test_simple_item_assignment(self):
        self.assertEqual(self.ring[2], 2)
        self.ring[2] = 4
        self.assertEqual(self.ring[2], 4)

    def test_item_assignment_loops_both_ways(self):
        self.ring[5] = 10
        self.assertEqual(self.ring._ring, [10, 1, 2, 3, 4])
        self.ring[21] = 11
        self.assertEqual(self.ring._ring, [10, 11, 2, 3, 4])
        self.ring[-3] = 20
        self.assertEqual(self.ring._ring, [10, 11, 20, 3, 4])
        self.ring[-7] = 30
        self.assertEqual(self.ring._ring, [10, 11, 20, 30, 4])

    def test_slice_assignment(self):
        self.ring[2:5] = [1, 2, 3]
        self.assertEqual(self.ring._ring, [0, 1, 1, 2, 3])

    def test_slice_assignment_loops(self):
        self.assertEqual(self.ring[5:8], [0, 1, 2])
        self.ring[5:8] = [10, 11, 12]
        self.assertEqual(self.ring._ring, [10, 11, 12, 3, 4])

    def test_reverse_part_of_ring(self):
        self.ring[1:4] = self.ring[3:0:-1]
        self.assertEqual(self.ring._ring, [0, 3, 2, 1, 4])


if __name__ == '__main__':
    unittest.main()
