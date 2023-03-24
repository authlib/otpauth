OTP Auth
========

One time password implementations in Python. HOTP and TOTP.

**Documentation**: https://otp.authlib.org/
**GitHub**: https://github.com/authlib/otpauth

Usage
-----

Most of the time, you would use a time based one time password. You can generate and
verify the token with ``HOTP``::

    import otpauth

    totp = otpauth.HOTP(b"user-secret")

    # generate a code for now
    code: int = totp.generate()

    # you may want to convert it to string
    str_code: str = totp.string_code(code)

    # verify the code
    totp.verify(code)  # => True
    totp.verify(str_code)  # => True
