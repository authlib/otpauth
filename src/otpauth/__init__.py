from .core import SupportedAlgorithms
from .rfc4226 import HOTP, generate_hotp
from .rfc6238 import TOTP, generate_totp


__author__ = "Hsiaoming Yang <me@lepture.com>"
__homepage__ = "https://github.com/lepture/otpauth"
__version__ = "2.1.1"

__all__ = [
    "SupportedAlgorithms",
    "HOTP",
    "TOTP",
    "generate_hotp",
    "generate_totp",
]
