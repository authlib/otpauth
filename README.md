<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/_static/dark-logo.svg">
  <img alt="OTP Auth logo" src="docs/_static/light-logo.svg" height="68">
</picture>

One time password implementations in Python. HOTP and TOTP.

[![Github Actions](https://github.com/authlib/otpauth/actions/workflows/tests.yml/badge.svg)](https://github.com/authlib/otpauth/actions/workflows/tests.yml)
[![PyPI](https://badgen.net/pypi/v/otpauth)](https://pypi.org/project/otpauth)
[![codecov](https://codecov.io/gh/authlib/otpauth/branch/main/graph/badge.svg?token=pWQIlZ9Ir4)](https://codecov.io/gh/authlib/otpauth)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=authlib_otpauth&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=authlib_otpauth)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=authlib_otpauth&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=authlib_otpauth)

</div>

## Usage

A quick and simple usage of ``HOTP``:

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

## Install

Install with pip:

```shell
pip install otpauth
```

## Useful links

- Documentation: https://otp.authlib.org/
- Blog: https://blog.authlib.org/
- Twitter: https://twitter.com/authlib

## Copyright

2013, Hsiaoming Yang. Under BSD-3 license.
