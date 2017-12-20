import unittest

from knot_hash import Ring, KnotHash


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


class KnotTest(unittest.TestCase):
    def setUp(self):
        self.knot_hash = KnotHash()
        self.knot_hash.ring = Ring(range(5))

    def test_individual_example_knots(self):
        self.knot_hash.tie_knot(position=0, length=3)
        self.assertEqual(self.knot_hash.ring._ring, [2, 1, 0, 3, 4])
        self.knot_hash.tie_knot(position=3, length=4)
        self.assertEqual(self.knot_hash.ring._ring, [4, 3, 0, 1, 2])
        self.knot_hash.tie_knot(position=3, length=1)
        self.assertEqual(self.knot_hash.ring._ring, [4, 3, 0, 1, 2])
        self.knot_hash.tie_knot(position=1, length=5)
        self.assertEqual(self.knot_hash.ring._ring, [3, 4, 2, 1, 0])

    def test_tie_all_knots(self):
        self.knot_hash.tie_all_knots(lengths=[3, 4, 1, 5])
        self.assertEqual(self.knot_hash.ring._ring, [3, 4, 2, 1, 0])


class KnotHashTest(unittest.TestCase):
    def setUp(self):
        self.knot_hash = KnotHash()

    def test_get_lengths_from_string(self):
        lengths = self.knot_hash.get_lengths_from_string('1,2,3')
        self.assertEqual(lengths, [49, 44, 50, 44, 51, 17, 31, 73, 47, 23])

    def test_preserve_skip_and_position(self):
        self.assertEqual(self.knot_hash.position, 0)
        self.assertEqual(self.knot_hash.skip, 0)
        self.knot_hash.tie_all_knots(lengths=[3, 4])
        self.assertEqual(self.knot_hash.position, 3 + 4 + 1)
        self.assertEqual(self.knot_hash.skip, 2)

    def test_reduce_sparse_hash(self):
        # Change single value, otherwise the result will be zero
        self.knot_hash.ring[47] = 1
        hash_values = self.knot_hash.reduce_sparse_hash()
        # Calculated manually
        self.assertEqual(hash_values[2], 46)

    def test_example_hashes(self):
        knot_hash = KnotHash()
        h = knot_hash.calculate_hash('')
        self.assertEqual(h, 'a2582a3a0e66e6e86e3812dcb672a272')

        knot_hash = KnotHash()
        h = knot_hash.calculate_hash('AoC 2017')
        self.assertEqual(h, '33efeb34ea91902bb2f59c9920caa6cd')

        knot_hash = KnotHash()
        h = knot_hash.calculate_hash('1,2,3')
        self.assertEqual(h, '3efbe78a8d82f29979031a4aa0b16a9d')

        knot_hash = KnotHash()
        h = knot_hash.calculate_hash('1,2,4')
        self.assertEqual(h, '63960835bcdc130f0b66d7ff4f6a5a8e')


if __name__ == '__main__':
    unittest.main()
