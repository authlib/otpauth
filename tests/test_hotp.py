import unittest
from otpauth import HOTP


class TestHOTP(unittest.TestCase):
    def setUp(self):
        self.hotp = HOTP(b"python")

    def test_generate(self):
        value = self.hotp.generate(0)
        self.assertEqual(value, 170566)

    def test_verify(self):
        # due to number too long
        self.assertFalse(self.hotp.verify(12345678, 0))

        # due to not match
        self.assertFalse(self.hotp.verify(12345, 0))

        self.assertTrue(self.hotp.verify(170566, 0))

    def test_to_uri(self):
        uri = self.hotp.to_uri("Typlog:lepture.com", "Authlib", 0)
        expected = "otpauth://hotp/Typlog:lepture.com?secret=OB4XI2DPNY&issuer=Authlib&algorithm=SHA1&digits=6&counter=0"
        self.assertEqual(uri, expected)

    def test_from_b32encode(self):
        expected = "otpauth://hotp/Typlog:lepture.com?secret=OB4XI2DPNY&issuer=Authlib&algorithm=SHA1&digits=6&counter=0"

        hotp = HOTP.from_b32encode("OB4XI2DPNY")
        value = hotp.generate(0)
        self.assertEqual(value, 170566)
        uri = self.hotp.to_uri("Typlog:lepture.com", "Authlib", 0)
        self.assertEqual(uri, expected)

        hotp = HOTP.from_b32encode("OB4XI2DPNY======")
        value = hotp.generate(0)
        self.assertEqual(value, 170566)
        uri = self.hotp.to_uri("Typlog:lepture.com", "Authlib", 0)
        self.assertEqual(uri, expected)

        hotp = HOTP.from_b32encode(b"OB4XI2DPNY======")
        value = hotp.generate(0)
        self.assertEqual(value, 170566)
        uri = self.hotp.to_uri("Typlog:lepture.com", "Authlib", 0)
        self.assertEqual(uri, expected)
