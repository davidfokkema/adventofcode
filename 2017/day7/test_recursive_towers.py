import io
import unittest
from unittest.mock import patch

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

    def test_get_balanced_tower_weight_simple_case(self):
        programs = {'foo': {'weight': 10, 'children': []}}
        weight = tower.get_balanced_tower_weight(programs, 'foo')
        self.assertEqual(weight, 10)

    def test_get_balanced_tower_weight_includes_children(self):
        programs = {'foo': {'weight': 10, 'children': ['bar', 'baz', 'hoi']},
                    'bar': {'weight': 11, 'children': []},
                    'baz': {'weight': 5, 'children': ['gee']},
                    'gee': {'weight': 6, 'children': []},
                    'hoi': {'weight': 11, 'children': []}}
        weight = tower.get_balanced_tower_weight(programs, 'foo')
        self.assertEqual(weight, 43)

    @patch.object(tower, 'raise_if_unbalanced')
    def test_get_balanced_tower_weight_calls_raise_if_unbalanced(
            self, mock_unbalanced):

        programs = {'foo': {'weight': 10, 'children': ['bar', 'baz']},
                    'bar': {'weight': 11, 'children': []},
                    'baz': {'weight': 12, 'children': []}}
        tower.get_balanced_tower_weight(programs, 'foo')
        mock_unbalanced.assert_called_once_with(programs, ['bar', 'baz'],
                                                [11, 12])

    def test_raise_if_unbalanced_raises_exception(self):
        # baz needs to have a weight of 5 to balance the tower
        programs = {'foo': {'weight': 10, 'children': ['bar', 'baz', 'hoi']},
                    'bar': {'weight': 11, 'children': []},
                    'baz': {'weight': 2, 'children': ['gee']},
                    'gee': {'weight': 6, 'children': []},
                    'hoi': {'weight': 11, 'children': []}}
        with self.assertRaises(tower.UnbalancedException) as cm:
            tower.raise_if_unbalanced(programs, ['bar', 'baz', 'hoi'],
                                      [11, 8, 11])
        raised_exception = cm.exception
        self.assertEqual(raised_exception.correct_weight, 5)


if __name__ == '__main__':
    unittest.main()
