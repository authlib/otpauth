OTP Auth
========

One time password implementations in Python. HOTP and TOTP.

.. note::

    This is a redesigned "v2" of otpauth. Get "v1" documentation
    at https://pythonhosted.org/otpauth/.

"v1" is considered stable, you may still use it. But "v2" has some
enhancements:

- **Type hints**: your editor will love it.
- **No Python 2**: clean code without compatible patches.

Installation
------------

Installing otpauth is simple with ``pip``::

    $ pip install otpauth

Simple Guide
------------

Most of the time, you would use a time based one time password. You can generate and
verify the token with :class:`TOTP`::

    import otpauth

    totp = otpauth.HOTP(b"user-secret")

    # generate a code for now
    code: int = totp.generate()

    # you may want to convert it to string
    str_code: str = totp.string_code(code)

    # verify the code
    totp.verify(code)  # => True
    totp.verify(str_code)  # => True

.. note:: To learn more about ``TOTP``, head over to :ref:`totp`.

Next Steps
----------

.. toctree::
    :caption: Guide

    recipes
    api

.. toctree::
    :caption: Development

    alternatives
    contribute
    changelog
