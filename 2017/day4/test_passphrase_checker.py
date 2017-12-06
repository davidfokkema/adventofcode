from collections import OrderedDict
import unittest

import passphrase_checker as pc


# I like my tests ordered on difficulty level
VALID_PASSPHRASES = OrderedDict([('aa bb cc dd ee', True),
                                 ('aa bb cc dd aa', False),
                                 ('aa bb cc dd aaa', True)])


class PassphraseCheckerTest(unittest.TestCase):
    def test_passphrase_checker(self):
        for phrase, is_valid in VALID_PASSPHRASES.items():
            self.assertEqual(pc.is_valid(phrase), is_valid)


if __name__ == '__main__':
    unittest.main()
