from ._rfc4226 import HOTP
from ._rfc4226 import generate_hotp
from ._rfc6238 import TOTP
from ._rfc6238 import generate_totp
from .core import SupportedAlgorithms

__author__ = "Hsiaoming Yang <me@lepture.com>"
__homepage__ = "https://otp.authlib.org/"
__version__ = "2.1.1"

__all__ = [
    "SupportedAlgorithms",
    "HOTP",
    "TOTP",
    "generate_hotp",
    "generate_totp",
]
