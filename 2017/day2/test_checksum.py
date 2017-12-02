import unittest

from checksum import checksum


class ChecksumTest(unittest.TestCase):
    def test_checksum(self):
        self.assertEqual(checksum('test_input'), 18)


if __name__ == '__main__':
    unittest.main()
