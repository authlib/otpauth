API References
==============

.. rst-class:: lead

   Here are the list of API reference; it might be helpful for developers.

----

.. module:: otpauth

HOTP
----

Implementation of RFC4226, An HMAC-Based One-Time Password Algorithm.

.. autoclass:: HOTP
   :members:
   :inherited-members:

.. autofunction:: generate_hotp

TOTP
----

Implementation of RFC6238, Time-Based One-Time Password Algorithm.

.. autoclass:: TOTP
   :members:
   :inherited-members:

.. autofunction:: generate_totp
