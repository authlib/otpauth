import unittest
from otpauth import HOTP, TOTP


class TestMisc(unittest.TestCase):
    def test_invalid_digit(self):
        self.assertRaises(AssertionError, HOTP, b"secret", 0)
        self.assertRaises(AssertionError, TOTP, b"secret", 0)

        self.assertRaises(AssertionError, HOTP, b"secret", 11)
        self.assertRaises(AssertionError, TOTP, b"secret", 11)

    def test_invalid_algorithm(self):
        self.assertRaises(AssertionError, HOTP, b"secret", algorithm="SHA2")
        self.assertRaises(AssertionError, TOTP, b"secret", algorithm="SHA2")

    def test_string_code(self):
        htop = HOTP(b"secret")
        self.assertEqual(htop.string_code(123), "000123")
