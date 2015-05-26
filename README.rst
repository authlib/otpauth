otpauth
=======

cryptography_ has built-in two factor support now.

.. _cryptography: https://github.com/pyca/cryptography

otpauth is One Time Password Authentication, which is usually called as
two steps verification. You may have heard it from Google, Dropbox and
etc.

.. image:: https://pypip.in/wheel/otpauth/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/otpauth/
   :alt: Wheel Status
.. image:: https://pypip.in/version/otpauth/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/otpauth/
   :alt: Latest Version
.. image:: https://travis-ci.org/lepture/otpauth.svg?branch=master
   :target: https://travis-ci.org/lepture/otpauth
   :alt: Travis CI Status
.. image:: https://coveralls.io/repos/lepture/otpauth/badge.svg?branch=master
   :target: https://coveralls.io/r/lepture/otpauth
   :alt: Coverage Status
.. image:: https://ci.appveyor.com/api/projects/status/x1rqksux15hicutq/branch/master
   :target: https://ci.appveyor.com/project/lepture/otpauth
   :alt: App Veyor CI Status

Installation
------------

Installing otpauth is simple with pip_::

    $ pip install otpauth

or, with easy_install_::

    $ easy_install otpauth


.. _pip: http://www.pip-installer.org/
.. _easy_install: http://pypi.python.org/pypi/setuptools


Usage
-----

Generate and validate an otp code is very simple::

    >>> from otpauth import OtpAuth
    >>> auth = OtpAuth('secret')  # a secret string
    >>> auth.hotp()  # generate a count based code, default count is 4
    330810
    >>> auth.valid_hotp(330810)
    4
    >>> auth.hotp(2)  # generate a count based code, count is 2
    720111
    >>> auth.valid_hotp(720111)
    2
    >>> auth.totp()  # generate a time based code
    828657
    >>> auth.valid_totp(828657)
    True


Authenticator
-------------

You can create a QR code for Google Authenticator to scan::

    >>> from otpauth import OtpAuth
    >>> auth = OtpAuth('secret')  # a secret string
    >>> s = auth.to_uri('totp', 'Example:foo@bar.baz', 'Foo')
    >>> import qrcode
    >>> img = qrcode.make(s)
