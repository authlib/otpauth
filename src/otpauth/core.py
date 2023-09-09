import base64
import typing as t
from urllib.parse import quote
from abc import ABCMeta, abstractmethod

SupportedAlgorithms = t.Literal["SHA1", "SHA256", "SHA512"]
Self = t.TypeVar("Self", bound="OTP")


class OTP(metaclass=ABCMeta):
    TYPE: t.ClassVar[str]

    #: The supportted algorithms
    ALGORITHMS: t.ClassVar[t.List[str]] = ["SHA1", "SHA256", "SHA512"]

    def __init__(self, secret: bytes, digit: int = 6, algorithm: SupportedAlgorithms = "SHA1"):
        assert 0 < digit < 11
        assert algorithm in self.ALGORITHMS

        self.secret = secret
        self.digit = digit
        self.algorithm = algorithm
        self._b32_secret: t.Optional[str] = None

    @property
    def b32_secret(self) -> str:
        if self._b32_secret:
            return self._b32_secret

        secret = base64.b32encode(self.secret)
        self._b32_secret = secret.rstrip(b"=").decode("ascii")
        return self._b32_secret

    @classmethod
    def from_b32encode(
            cls: t.Type[Self],
            secret: t.Union[bytes, str],
            digit: int = 6,
            algorithm: SupportedAlgorithms = "SHA1") -> Self:
        """Create the instance with a base32 encoded secret.

        :param secret: A base32 encoded secret string or bytes.
        :param digit: Number of digits in the OTP code.
        :param algorithm: Hash algorithm used in HOTP.
        """
        if isinstance(secret, str):
            secret = secret.encode("utf-8")

        b32_secret = secret.rstrip(b"=")

        # add padding back
        secret += b"=" * (-len(secret) % 8)
        raw_secret = base64.b32decode(secret)

        obj = cls(raw_secret, digit, algorithm)
        obj._b32_secret = b32_secret.decode("ascii")
        return obj

    def _get_base_uri(self, label: str, issuer: str) -> str:
        label = quote(label, safe="/@:")
        issuer = quote(issuer, safe="")
        _type = self.TYPE.lower()
        url = (
            f"otpauth://{_type}/{label}"
            f"?secret={self.b32_secret}"
            f"&issuer={issuer}"
            f"&algorithm={self.algorithm}"
            f"&digits={self.digit}"
        )
        return url

    def string_code(self, code: int) -> str:
        """Add leading 0 if the code length does not match the defined length.

        For instance, parameter ``digit=6``, but ``code=123``, this method would
        return ``000123``::

            >>> otp.string_code(123)
            '000123'

        :param code: The number that this OTP generated.
        """
        return f'{code:0{self.digit}}'

    @abstractmethod
    def generate(self, *args: t.Any, **kwargs: t.Any) -> int:
        ...

    @abstractmethod
    def verify(self, code: int, *args: t.Any, **kwargs: t.Any) -> bool:
        ...

    @abstractmethod
    def to_uri(self, label: str, issuer: str, *args: t.Any, **kwargs: t.Any) -> str:
        ...
