import base64
import typing as t
from urllib.parse import quote
from abc import ABCMeta, abstractmethod


class OTP(object, metaclass=ABCMeta):
    TYPE: str
    ALGORITHMS = ["SHA1", "SHA256", "SHA512"]

    def __init__(self, secret: bytes, digit: int = 6, algorithm: str = "SHA1"):
        assert algorithm in self.ALGORITHMS

        self.secret = secret
        self.digit = digit
        self.algorithm = algorithm
        self._b32_secret = None

    @property
    def b32_secret(self) -> str:
        if self._b32_secret:
            return self._b32_secret

        secret = base64.b32encode(self.secret)
        self._b32_secret = secret.rstrip(b'=').decode("ascii")
        return self._b32_secret

    @classmethod
    def from_b32encode(cls, secret: t.AnyStr):
        if isinstance(secret, str):
            secret = secret.encode("utf-8")

        b32_secret = secret.rstrip(b'=')

        # add padding back
        secret += b'=' * (-len(secret) % 8)
        raw_secret = base64.b32decode(secret)

        obj = cls(raw_secret)
        obj._b32_secret = b32_secret.decode("ascii")
        return obj

    def _get_base_uri(self, label: str, issuer: str) -> str:
        label = quote(label, safe="/@:")
        issuer = quote(issuer, safe="")
        _type = self.TYPE.lower()
        return f"otpauth://{_type}/{label}?secret={self.b32_secret}&issuer={issuer}&algorithm={self.algorithm}&digits={self.digit}"

    @abstractmethod
    def generate(self, *args, **kwargs) -> int:
        ...

    @abstractmethod
    def verify(self, code: int, *args, **kwargs) -> bool:
        ...

    @abstractmethod
    def to_uri(self, label: str, issuer: str, *args, **kwargs) -> str:
        ...
