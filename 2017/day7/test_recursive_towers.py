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


class RecursiveTowerTest(unittest.TestCase):
    def test_find_bottom_program(self):
        with io.StringIO(EXAMPLE_INPUT) as f:
            input_data = f.readlines()
        bottom = tower.find_bottom_program(input_data)
        self.assertEqual(bottom, 'tknk')

    def test_find_upper_programs(self):
        with io.StringIO(EXAMPLE_INPUT) as f:
            input_data = f.readlines()
        upper_programs = tower.find_upper_programs(input_data)
        self.assertIn('ktlj', upper_programs)
        self.assertIn('qoyq', upper_programs)
        self.assertIn('ebii', upper_programs)
        self.assertNotIn('tknk', upper_programs)


if __name__ == '__main__':
    unittest.main()
