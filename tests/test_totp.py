import unittest
import time
from otpauth import TOTP

FIXED_TIME = 1679576495


class TestTOTP(unittest.TestCase):
    def setUp(self):
        self.totp = TOTP(b"python")

    def test_generate(self):
        value = self.totp.generate(FIXED_TIME)
        self.assertEqual(value, 129815)

    def test_verify(self):
        # due to number too long
        self.assertFalse(self.totp.verify(12345678, FIXED_TIME))

        # due to not match
        self.assertFalse(self.totp.verify(12345, FIXED_TIME))

        self.assertTrue(self.totp.verify(129815, FIXED_TIME))

    def test_to_uri(self):
        uri = self.totp.to_uri("Typlog:lepture.com", "Authlib")
        expected = "otpauth://totp/Typlog:lepture.com?secret=OB4XI2DPNY&issuer=Authlib&algorithm=SHA1&digits=6&period=30"
        self.assertEqual(uri, expected)

    def test_current_timestamp(self):
        value = self.totp.generate()
        self.assertTrue(self.totp.verify(value))
