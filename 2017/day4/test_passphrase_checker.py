import unittest
from unittest.mock import patch, mock_open, sentinel

import passphrase_checker as pc


VALID_PASSPHRASES = [('aa bb cc dd ee', True),
                     ('aa bb cc dd aa', False),
                     ('aa bb cc dd aaa', True)]


class PassphraseCheckerTest(unittest.TestCase):
    def test_passphrase_checker(self):
        for phrase, is_valid in VALID_PASSPHRASES:
            self.assertEqual(pc.is_valid(phrase), is_valid)

    def test_count_valid_passphrases(self):
        read_data = '\n'.join([u[0] for u in VALID_PASSPHRASES])
        mock = mock_open(read_data=read_data)
        with patch('passphrase_checker.open', mock):
            sum = pc.count_valid_passphrases(sentinel.filename)
            mock.assert_called_once_with(sentinel.filename)
            self.assertEqual(sum, 2)


if __name__ == '__main__':
    unittest.main()
