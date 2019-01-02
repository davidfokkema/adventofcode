import unittest

from fabric import calculate_claim_size, calculate_fabric_size


claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']


class FabricTest(unittest.TestCase):
    def test_calculate_claim_size(self):
        self.assertEqual(calculate_claim_size(claims[0]), (5, 7))
        self.assertEqual(calculate_claim_size(claims[1]), (7, 5))
        self.assertEqual(calculate_claim_size(claims[2]), (7, 7))

    def test_calculate_fabric_size(self):
        self.assertEqual(calculate_fabric_size(claims), (7, 7))


if __name__ == '__main__':
    unittest.main()
