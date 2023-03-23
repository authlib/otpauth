from .rfc4226 import HOTP, generate_hotp
from .rfc6238 import TOTP, generate_totp


__author__ = 'Hsiaoming Yang <me@lepture.com>'
__homepage__ = 'https://github.com/lepture/otpauth'
__version__ = '2.0.0'

__all__ = [
    "HOTP", "TOTP",
    "generate_hotp",
    "generate_totp",
]
