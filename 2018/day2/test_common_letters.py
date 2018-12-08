import unittest

from common_letters import (find_common_letters_in_two_strings,
                            find_common_letters)


class CommonLettersTest(unittest.TestCase):
    def test_find_common_letters_in_two_strings(self):
        self.assertEqual(find_common_letters_in_two_strings('fghij', 'fguij'),
                         'fgij')

    def test_find_common_letters(self):
        string_list = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye',
                       'wvxyz']
        self.assertEqual(find_common_letters(string_list), 'fgij')


if __name__ == '__main__':
    unittest.main()
