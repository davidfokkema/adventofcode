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

    def test_raises_exception_when_empty(self):
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


if __name__ == '__main__':
    unittest.main()
