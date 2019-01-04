import unittest

from alchemical_reduction import (reduce_polymer, remove_type_and_react,
                                  find_length_of_shortest_polymer)


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

    def test_remove_type_and_react(self):
        polymer = "dabAcCaCBAcCcaDA"
        self.assertEqual(remove_type_and_react(polymer, 'a'), "dbCBcD")
        self.assertEqual(remove_type_and_react(polymer, 'c'), "daDA")

    def test_find_length_of_shortest_polymer(self):
        polymer = "dabAcCaCBAcCcaDA"
        self.assertEqual(find_length_of_shortest_polymer(polymer), 4)


if __name__ == '__main__':
    unittest.main()
