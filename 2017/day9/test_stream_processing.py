from io import StringIO
import unittest

from stream_processing import StreamProcessor


class RemoveGarbageTest(unittest.TestCase):
    def setUp(self):
        self.processor = StreamProcessor()

    def eat_garbage_test(self, garbage):
        # Keep in mind: first < is already eaten before passing on to
        # eat_garbage()
        with StringIO(garbage[1:]) as s:
            self.processor.eat_garbage(s)
            rest = s.read()
        self.assertEqual(rest, '')

    def test_raises_exception_when_stream_runs_out(self):
        with self.assertRaises(RuntimeError):
            self.eat_garbage_test('<')

    def test_empty_garbage(self):
        self.eat_garbage_test('<>')

    def test_random_garbage(self):
        self.eat_garbage_test('<random characters>')

    def test_ignore_start_codon(self):
        self.eat_garbage_test('<<<<>')

    def test_cancel_closing_marker(self):
        self.eat_garbage_test('<{!>}>')

    def test_cancel_cancel_marker(self):
        self.eat_garbage_test('<!!>')

    def test_handle_many_cancels(self):
        self.eat_garbage_test('<!!!>>')

    def test_complex_garbage(self):
        self.eat_garbage_test('<{o"i!a,<{i<a>')


class CountGarbageCharactersTest(unittest.TestCase):
    def setUp(self):
        self.processor = StreamProcessor()

    def eat_garbage_test(self, garbage, num_characters):
        # Keep in mind: first < is already eaten before passing on to
        # eat_garbage()
        with StringIO(garbage[1:]) as s:
            actual_num_characters = self.processor.eat_garbage(s)
            rest = s.read()
        self.assertEqual(rest, '')
        self.assertEqual(actual_num_characters, num_characters)

    def test_empty_garbage(self):
        self.eat_garbage_test('<>', num_characters=0)

    def test_long_garbage(self):
        self.eat_garbage_test('<random characters>', num_characters=17)

    def test_opening_garbage(self):
        self.eat_garbage_test('<<<<>', num_characters=3)

    def test_cancelled_garbage(self):
        self.eat_garbage_test('<{!>}>', num_characters=2)

    def test_doubly_cancelled_garbage(self):
        self.eat_garbage_test('<!!>', num_characters=0)

    def test_triple_cancelled_garbage(self):
        self.eat_garbage_test('<!!!>>', num_characters=0)

    def test_complex_garbage(self):
        self.eat_garbage_test('<{o"i!a,<{i<a>', num_characters=10)


class ProcessGroupTest(unittest.TestCase):
    def setUp(self):
        self.processor = StreamProcessor()

    def process_group_test(self, group, num_groups=0):
        # Keep in mind: first { is already eaten before passing on to
        # process_group()
        with StringIO(group[1:]) as s:
            actual_num_groups, _, _ = self.processor.process_group(s)
            rest = s.read()
        self.assertEqual(rest, '')
        self.assertEqual(actual_num_groups, num_groups)

    def test_raises_exception_when_stream_runs_out(self):
        with self.assertRaises(RuntimeError):
            self.process_group_test('{')

    def test_empty_group(self):
        self.process_group_test('{}', num_groups=1)

    def test_three_nested_groups(self):
        self.process_group_test('{{{}}}', num_groups=3)

    def test_three_sequential_groups(self):
        self.process_group_test('{{},{}}', num_groups=3)

    def test_mixed_groups(self):
        self.process_group_test('{{{},{},{{}}}}', num_groups=6)

    def test_mixed_group_garbage(self):
        self.process_group_test('{<{},{},{{}}>}', num_groups=1)

    def test_sequential_garbage(self):
        self.process_group_test('{<a>,<a>,<a>,<a>}', num_groups=1)

    def test_grouped_garbage(self):
        self.process_group_test('{{<a>},{<a>},{<a>},{<a>}}', num_groups=5)

    def test_cancelled_garbage(self):
        self.process_group_test('{{<!>},{<!>},{<!>},{<a>}}', num_groups=2)


class ProcessGroupScoreTest(unittest.TestCase):
    def setUp(self):
        self.processor = StreamProcessor()

    def process_group_score_test(self, group, score=0):
        # Keep in mind: first { is already eaten before passing on to
        # process_group()
        with StringIO(group[1:]) as s:
            _, actual_score, _ = self.processor.process_group(s)
            rest = s.read()
        self.assertEqual(rest, '')
        self.assertEqual(actual_score, score)

    def test_empty_group(self):
        self.process_group_score_test('{}', score=1)

    def test_three_nested_groups(self):
        self.process_group_score_test('{{{}}}', score=6)

    def test_three_sequential_groups(self):
        self.process_group_score_test('{{},{}}', score=5)

    def test_mixed_groups(self):
        self.process_group_score_test('{{{},{},{{}}}}', score=16)

    def test_sequential_garbage(self):
        self.process_group_score_test('{<a>,<a>,<a>,<a>}', score=1)

    def test_grouped_garbage(self):
        self.process_group_score_test('{{<ab>},{<ab>},{<ab>},{<ab>}}', score=9)

    def test_doubly_cancelled_garbage(self):
        self.process_group_score_test('{{<!!>},{<!!>},{<!!>},{<!!>}}', score=9)

    def test_mostly_cancelled_garbage(self):
        self.process_group_score_test('{{<a!>},{<a!>},{<a!>},{<ab>}}', score=3)


class CountGarbageWithinGroupsTest(unittest.TestCase):
    def setUp(self):
        self.processor = StreamProcessor()

    def process_group_garbage_test(self, group, num_garbage=0):
        # Keep in mind: first { is already eaten before passing on to
        # process_group()
        with StringIO(group[1:]) as s:
            _, _, actual_garbage = self.processor.process_group(s)
            rest = s.read()
        self.assertEqual(rest, '')
        self.assertEqual(actual_garbage, num_garbage)

    def test_empty_group(self):
        self.process_group_garbage_test('{}', num_garbage=0)

    def test_empty_garbage(self):
        self.process_group_garbage_test('{<>}', num_garbage=0)

    def test_simple_garbage(self):
        self.process_group_garbage_test('{<foo>}', num_garbage=3)

    def test_nested_simple_garbage(self):
        self.process_group_garbage_test('{{<foo>}}', num_garbage=3)

    def test_complex_garbage(self):
        self.process_group_garbage_test('{{<123>},<4567>,<89>}', num_garbage=9)



if __name__ == '__main__':
    unittest.main()
