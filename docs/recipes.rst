:description: Detail guide on how to use TOTP and HOTP.

User Guide
==========

.. rst-class:: lead

    Here are the detail guide on how to use TOTP and HOTP.

----

.. _totp:

Use TOTP
--------

TOTP is a **Time-Based One-Time Password Algorithm** defined in
RFC6238_.

.. _RFC6238: https://www.rfc-editor.org/rfc/rfc6238

.. code-block:: python

    import time
    from otpauth import TOTP

    totp = TOTP(b"user-secret")

    # generate a code for now
    code: int = totp.generate()

    totp.verify(code)  # True

    time.sleep(31)
    totp.verify(code)  # False

Most of the time, you DO NOT NEED TO change the default configuration,
but if you want, here is how:

.. code-block:: python

    totp = TOTP(b"user-secret", digit=8, algorithm="SHA256")

.. _hotp:

Use HOTP
--------

HOTP is a **An HMAC-Based One-Time Password Algorithm** defined in
RFC4226_.

.. _RFC4226: https://www.rfc-editor.org/rfc/rfc4226


.. code-block:: python

    from otpauth import HOTP

    htop = HOTP(b"user-secret")

    # generate a code for now
    code: int = htop.generate(4)

    htop.verify(code, 4)  # True
    htop.verify(code, 6)  # False

.. tip:: TOTP is based on HOTP, most of the time you would use HOTP.

Use ``base32`` Secret
---------------------

When the **secret** you have is a ``base32`` encoded string, you don't have to
decode it yourself. Instead, you can create the :class:`TOTP` and :class:`HTOP`
instance with:

.. code-block:: python

    totp = TOTP.from_b32encode("OB4XI2DPNY")
    hotp = HOTP.from_b32encode("OB4XI2DPNY")

It works well with and without the padding ``=``. e.g.:

.. code-block:: python

    totp = TOTP.from_b32encode("OB4XI2DPNY======")
    hotp = HOTP.from_b32encode("OB4XI2DPNY======")

This method also accepts secret in bytes.

Add to Authenticator App
------------------------

There is a method ``.to_uri`` to generate the URI that most authenticator apps
support. The `Key URI Format`_ looks like:


.. code-block:: text

    otpauth://TYPE/LABEL?PARAMETERS

.. _`Key URI Format`: https://github.com/google/google-authenticator/wiki/Key-Uri-Format

An example of :meth:`TOTP.to_uri`:

.. code-block:: python

    >>> totp = TOTP.from_b32encode("OB4XI2DPNY")
    >>> totp.to_uri("Typlog:lepture.com", "Authlib")
    "otpauth://totp/Typlog:lepture.com?secret=OB4XI2DPNY&issuer=Authlib&algorithm=SHA1&digits=6&period=30"

Here shows the QR code of this URI:

.. figure:: _static/example-qr.png
   :align: center
   :width: 160
   :height: 160

   You can test with an authenticator app.
