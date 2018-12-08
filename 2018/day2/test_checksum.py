import unittest

from checksum import has_letter_twice, has_letter_thrice, calculate_checksum


class ChecksumTest(unittest.TestCase):
    def test_has_letter_twice(self):
        self.assertFalse(has_letter_twice('abcdef'))
        self.assertTrue(has_letter_twice('bababc'))
        self.assertTrue(has_letter_twice('abbcde'))
        self.assertFalse(has_letter_twice('abcccd'))
        self.assertTrue(has_letter_twice('aabcdd'))
        self.assertTrue(has_letter_twice('abcdee'))
        self.assertFalse(has_letter_twice('ababab'))

    def test_has_letter_thrice(self):
        self.assertFalse(has_letter_thrice('abcdef'))
        self.assertTrue(has_letter_thrice('bababc'))
        self.assertFalse(has_letter_thrice('abbcde'))
        self.assertTrue(has_letter_thrice('abcccd'))
        self.assertFalse(has_letter_thrice('aabcdd'))
        self.assertFalse(has_letter_thrice('abcdee'))
        self.assertTrue(has_letter_thrice('ababab'))

    def test_checksum(self):
        strings = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee',
                   'ababab']
        self.assertEqual(calculate_checksum(strings), 12)


if __name__ == '__main__':
    unittest.main()
