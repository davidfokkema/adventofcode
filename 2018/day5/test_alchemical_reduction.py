import unittest

from alchemical_reduction import reduce_polymer


class AlchemicalReductionTest(unittest.TestCase):
    def test_reduce_polymer(self):
        self.assertEqual(reduce_polymer("bAab"), "bb")
        self.assertEqual(reduce_polymer("AAaa"), "")
        self.assertEqual(reduce_polymer("AacbC"), "cbC")
        self.assertEqual(reduce_polymer("dabAcCaCBAcCcaDA"), "dabCBAcaDA")

    def test_more_advanced_polymers(self):
        # when index hit -1, a valuerror was raised and the execution stopped
        self.assertEqual(reduce_polymer("AaBb"), "")
        self.assertEqual(reduce_polymer("AacBb"), "c")
        self.assertEqual(reduce_polymer("AaBbc"), "c")
        self.assertEqual(reduce_polymer("AaaBbc"), "ac")
        self.assertEqual(reduce_polymer("CAaaBbc"), "Cac")
        self.assertEqual(reduce_polymer("cAaBbC"), "")


if __name__ == '__main__':
    unittest.main()
