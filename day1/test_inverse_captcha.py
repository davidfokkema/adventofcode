import unittest

from inverse_captcha import inverse_captcha, oneline_inverse_captcha


class InverseCaptchaTest(unittest.TestCase):
    def test_results(self):
        self.assertEqual(inverse_captcha('1122'), 3)
        self.assertEqual(inverse_captcha('1111'), 4)
        self.assertEqual(inverse_captcha('1234'), 0)
        self.assertEqual(inverse_captcha('91212129'), 9)

    def test_oneline_results(self):
        self.assertEqual(oneline_inverse_captcha('1122'), 3)
        self.assertEqual(oneline_inverse_captcha('1111'), 4)
        self.assertEqual(oneline_inverse_captcha('1234'), 0)
        self.assertEqual(oneline_inverse_captcha('91212129'), 9)


if __name__ == '__main__':
    unittest.main()
