<div align="center">

# OTP Auth

One time password implementations in Python. HOTP and TOTP.

[![Github Actions](https://github.com/authlib/otpauth/actions/workflows/tests.yml/badge.svg)](https://github.com/authlib/otpauth/actions/workflows/tests.yml)
[![PyPI](https://badgen.net/pypi/v/authlib)](https://pypi.org/project/otpauth)
[![codecov](https://badgen.net/codecov/c/github/authlib/otpauth)](https://codecov.io/gh/authlib/otpauth)

</div>

Usage
-----

```python
import otpauth

totp = otpauth.HOTP(b"user-secret")

# generate a code for now
code: int = totp.generate()

# you may want to convert it to string
str_code: str = totp.string_code(code)

# verify the code
totp.verify(code)  # => True
totp.verify(str_code)  # => True
```

Copyright
---------

2013, Hsiaoming Yang. Under BSD-3 license.
