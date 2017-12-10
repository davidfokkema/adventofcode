import io
import unittest

import recursive_tower as tower


EXAMPLE_INPUT = """\
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""
with io.StringIO(EXAMPLE_INPUT) as f:
    INPUT_DATA = f.readlines()
    

class RecursiveTowerTest(unittest.TestCase):
    def test_find_bottom_program(self):
        bottom = tower.find_bottom_program(INPUT_DATA)
        self.assertEqual(bottom, 'tknk')

    def test_find_upper_programs(self):
        upper_programs = tower.find_upper_programs(INPUT_DATA)
        self.assertIn('ktlj', upper_programs)
        self.assertIn('qoyq', upper_programs)
        self.assertIn('ebii', upper_programs)
        self.assertNotIn('tknk', upper_programs)

    def test_build_tree_structure(self):
        tower_structure = tower.build_tree_structure(INPUT_DATA)
        self.assertEqual(tower_structure['qoyq'], {'weight': 66,
                                                   'children': []})
        self.assertEqual(tower_structure['ugml'], {'weight': 68,
                                                   'children': ['gyxo', 'ebii',
                                                                'jptl']})


if __name__ == '__main__':
    unittest.main()

