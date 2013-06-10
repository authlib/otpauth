One Time Password Authentication
================================

.. image:: https://travis-ci.org/lepture/otpauth.png?branch=master
        :target: https://travis-ci.org/lepture/otpauth
.. image:: https://coveralls.io/repos/lepture/otpauth/badge.png?branch=master
        :target: https://coveralls.io/r/lepture/otpauth


Installation
------------

To install otpauth, simply::

    $ pip install otpauth

Usage
-----

Generate and validate an otp code is very simple::

    >>> from otpauth import OtpAuth
    >>> auth = OtpAuth('secret')  # a secret string
    >>> auth.hotp()
    330810
    >>> auth.valid_hotp(330810)
    4
    >>> auth.hotp(2)
    720111
    >>> auth.valid_hotp(720111)
    2
    >>> auth.totp()  # a time based string
    828657
    >>> auth.valid_totp(828657)
    True


Google Authenticator
--------------------

You can create a QR code for Google Authenticator to scan::

    >>> from otpauth import OtpAuth
    >>> auth = OtpAuth('secret')  # a secret string
    >>> s = auth.to_google('totp', 'Example:foo@bar.baz', 'Foo')
    >>> import qrcode
    >>> img = qrcode.make(s)
