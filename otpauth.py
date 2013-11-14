# -*- coding: utf-8 -*-
"""
    otpauth
    ~~~~~~~

    Implements two-step verification of HOTP/TOTP.

    :copyright: (c) 2013 by Hsiaoming Yang.
    :license: BSD, see LICENSE for more details.
"""
import base64
import hashlib
import hmac
import struct
import sys
import time
import warnings


if sys.version_info[0] == 3:
    python_version = 3
    string_type = str
else:
    python_version = 2
    string_type = unicode
    range = xrange


__author__ = 'Hsiaoming Yang <me@lepture.com>'
__homepage__ = 'https://github.com/lepture/otpauth'
__version__ = '0.2.0'


__all__ = ['OtpAuth', 'HOTP', 'TOTP']


HOTP = 'hotp'
TOTP = 'totp'


class OtpAuth(object):
    """One Time Password Authentication.

    :param secret: A secret token for the authentication.
    """

    def __init__(self, secret):
        self.secret = secret

    def hotp(self, counter=4):
        """Generate a HOTP code.

        :param counter: HOTP is a counter based algorithm.
        """
        # https://tools.ietf.org/html/rfc4226
        msg = struct.pack('>Q', counter)
        digest = hmac.new(to_bytes(self.secret), msg, hashlib.sha1).digest()

        ob = digest[19]
        if python_version == 2:
            ob = ord(ob)

        pos = ob & 15
        base = struct.unpack('>I', digest[pos:pos + 4])[0] & 0x7fffffff
        token = base % 1000000
        return token

    def totp(self, period=30):
        """Generate a TOTP code.

        A TOTP code is an extension of HOTP algorithm.

        :param period: A period that a TOTP code is valid in seconds
        """
        # https://tools.ietf.org/html/rfc6238
        counter = int(time.time()) // period
        return self.hotp(counter)

    def valid_hotp(self, code, last=0, trials=100):
        """Valid a HOTP code.

        :param code: A number that is less than 6 characters.
        :param last: Guess HOTP code from last + 1 range.
        :param trials: Guest HOTP code end at last + trials + 1.
        """
        if not valid_code(code):
            return False

        code = int(code)
        for i in range(last + 1, last + trials + 1):
            if self.hotp(counter=i) == code:
                return i
        return False

    def valid_totp(self, code, period=30):
        """Valid a TOTP code.

        :param code: A number that is less than 6 characters.
        :param period: A period that a TOTP code is valid in seconds
        """
        return valid_code(code) and self.totp(period) == int(code)

    def to_uri(self, type, label, issuer, counter=None):
        """Generate the otpauth protocal string.

        :param type: Algorithm type, hotp or totp.
        :param label: Label of the identifier.
        :param issuer: The company, the organization or something else.
        :param counter: Counter of the HOTP algorithm.
        """
        type = type.lower()

        if type not in ('hotp', 'totp'):
            raise ValueError('type must be hotp or totp')

        if type == 'hotp' and not counter:
            raise ValueError('HOTP type authentication need counter')

        secret = base64.b32encode(to_bytes(self.secret))
        # bytes to string
        secret = secret.decode('utf-8')
        # remove pad string
        secret = secret.strip('=')

        # https://code.google.com/p/google-authenticator/wiki/KeyUriFormat
        url = ('otpauth://%(type)s/%(label)s?secret=%(secret)s'
               '&issuer=%(issuer)s')
        dct = dict(
            type=type, label=label, issuer=issuer,
            secret=secret, counter=counter
        )
        ret = url % dct
        if type == 'hotp':
            ret = '%s&counter=%s' % (ret, counter)
        return ret

    def to_google(self, type, label, issuer, counter=None):
        """Generate the otpauth protocal string for Google Authenticator.

        .. deprecated:: 0.2.0
           Use :func:`to_uri` instead.
        """
        warnings.warn('deprecated, use to_uri instead', DeprecationWarning)
        return self.to_uri(type, label, issuer, counter)


def to_bytes(text):
    if isinstance(text, string_type):
        # Python3 str -> bytes
        # Python2 unicode -> str
        text = text.encode('utf-8')
    return text


def valid_code(code):
    code = string_type(code)
    return code.isdigit() and len(code) <= 6
