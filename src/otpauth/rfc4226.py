import struct
import hmac
import hashlib
from .core import OTP


class HOTP(OTP):
    """Implementation of RFC4226, An HMAC-Based One-Time Password Algorithm.

    :param secret: A secret in bytes
    :param digit: Number of digits in the HOTP code.
    :param algorithm: Hash algorithm used in HOTP.
    """

    TYPE = "HOTP"

    def generate(self, counter: int) -> int:
        """Generate a HOTP code. The returning result is an integer.
        To convert it into string with the correct digit length, developers
        can use :meth:`string_code`::

            int_code = hotp.generate(4)
            str_code = hotp.string_code(int_code)

        :param counter: HOTP is a counter based algorithm.
        """
        return generate_hotp(self.secret, counter, self.digit, self.algorithm)

    def verify(self, code: int, counter: int) -> bool:
        """Valid a HOTP code at the given counter.

        :param code: A number to be verified.
        :param counter: The counter HOTP code based on.
        """
        if len(str(code)) > self.digit:
            return False
        return hmac.compare_digest(bytes(self.generate(counter)), bytes(code))

    def to_uri(self, label: str, issuer: str, counter: int) -> str:
        """Generate the otpauth protocal string for HOTP.

        :param label: Label of the identifier.
        :param issuer: The company, the organization or something else.
        :param counter: Initial counter of the HOTP algorithm.
        """
        uri = self._get_base_uri(label, issuer)
        return uri + f"&counter={counter}"


def generate_hotp(secret: bytes, counter: int, digit: int=6, algorithm: str = "SHA1") -> int:
    """Generate a HOTP code.

    :param secret: A secret token for the authentication.
    :param counter: HOTP is a counter based algorithm.
    :param digit: Number of digits in the HOTP code.
    :param algorithm: Hash algorithm used in HOTP.
    """
    hash_alg = getattr(hashlib, algorithm.lower())
    msg = struct.pack('>Q', counter)
    digest = hmac.new(secret, msg, hash_alg).digest()
    offset = digest[19] & 0xf
    bin_code: int = struct.unpack('>I', digest[offset:offset + 4])[0]
    base = bin_code & 0x7fffffff
    return base % (10 ** digit)
