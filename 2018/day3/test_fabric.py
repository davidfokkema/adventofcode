import unittest

from fabric import Fabric


claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']


class FabricTest(unittest.TestCase):
    def setUp(self):
        self.fabric = Fabric(claims)
        self.fabric.process_claims()

    def test_calculate_claim_size(self):
        self.assertEqual(self.fabric.calculate_claim_size(claims[0]), (5, 7))
        self.assertEqual(self.fabric.calculate_claim_size(claims[1]), (7, 5))
        self.assertEqual(self.fabric.calculate_claim_size(claims[2]), (7, 7))

    def test_calculate_fabric_size(self):
        self.assertEqual(self.fabric.calculate_fabric_size(claims), (7, 7))

    def test_process_claims(self):
        self.assertEqual(self.fabric.fabric[0, 0], 0)
        self.assertEqual(self.fabric.fabric[3, 1], 1)
        self.assertEqual(self.fabric.fabric[2, 3], 1)
        self.assertEqual(self.fabric.fabric[3, 3], 2)

    def test_count_overlapping_squares(self):
        self.assertEqual(self.fabric.count_overlapping_squares(), 4)

    def test_check_intact_claim(self):
        self.assertEqual(self.fabric.check_intact_claim(claims[0]), False)
        self.assertEqual(self.fabric.check_intact_claim(claims[1]), False)
        self.assertEqual(self.fabric.check_intact_claim(claims[2]), True)

    def test_find_intact_claim_id(self):
        self.assertEqual(self.fabric.find_intact_claim_id(), 3)


if __name__ == '__main__':
    unittest.main()
