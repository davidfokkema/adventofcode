import unittest

import passphrase_checker as pc


class PassphraseCheckerTest(unittest.TestCase):
    def test_passphrase_checker(self):
        self.assertTrue(pc.is_valid('aa bb cc dd ee'))
        self.assertFalse(pc.is_valid('aa bb cc dd aa'))
        self.assertTrue(pc.is_valid('aa bb cc dd aaa'))


if __name__ == '__main__':
    unittest.main()
