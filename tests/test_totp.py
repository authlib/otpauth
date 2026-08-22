import unittest

from otpauth import TOTP

FIXED_TIME = 1679576495


class TestTOTP(unittest.TestCase):
    def setUp(self):
        self.totp = TOTP(b"python")

    def test_generate(self):
        value = self.totp.generate(FIXED_TIME)
        self.assertEqual(value, 129815)

    def test_rfc6238_vectors(self):
        times = [59, 1111111109, 1111111111, 1234567890, 2000000000, 20000000000]
        vectors = {
            "SHA1": (
                b"12345678901234567890",
                [94287082, 7081804, 14050471, 89005924, 69279037, 65353130],
            ),
            "SHA256": (
                b"12345678901234567890123456789012",
                [46119246, 68084774, 67062674, 91819424, 90698825, 77737706],
            ),
            "SHA512": (
                b"1234567890123456789012345678901234567890123456789012345678901234",
                [90693936, 25091201, 99943326, 93441116, 38618901, 47863826],
            ),
        }

        for algorithm, (secret, expected) in vectors.items():
            totp = TOTP(secret, digit=8, algorithm=algorithm)
            self.assertEqual([totp.generate(timestamp) for timestamp in times], expected)

    def test_verify(self):
        # due to number too long
        self.assertFalse(self.totp.verify(12345678, FIXED_TIME))

        # due to not match
        self.assertFalse(self.totp.verify(12345, FIXED_TIME))
        self.assertFalse(self.totp.verify("●●●●●●", FIXED_TIME))

        self.assertTrue(self.totp.verify(129815, FIXED_TIME))

    def test_to_uri(self):
        uri = self.totp.to_uri("Typlog:lepture.com", "Authlib")
        expected = (
            "otpauth://totp/Typlog:lepture.com?secret=OB4XI2DPNY&issuer=Authlib&algorithm=SHA1&digits=6&period=30"
        )
        self.assertEqual(uri, expected)

    def test_current_timestamp(self):
        value = self.totp.generate()
        self.assertTrue(self.totp.verify(value))
