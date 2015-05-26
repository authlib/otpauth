
Changelog
----------

Here is the full history of otpauth.

Version 1.0.1
~~~~~~~~~~~~~

Released on May 26, 2015

Use ``compare_digest`` to avoid timing attack.

Version 1.0
~~~~~~~~~~~

Released on Jan 25, 2015

Nothing new. It is stable now.

Version 0.3.0
~~~~~~~~~~~~~

Released on Dec 18, 2014

* Make ``generate_hotp`` and ``generate_totp`` functions.
* Add ``timestamp`` parameters for ``generate_totp``. `#3`_

.. _`#3`: https://github.com/lepture/otpauth/pull/3


Version 0.2.0
~~~~~~~~~~~~~

Released on Nov 14, 2013

* Change API name ``to_google`` to ``to_uri``.

Version 0.1.2
~~~~~~~~~~~~~

Released on Aug 16, 2013

* Raise ValueError instead of TypeError when parameters are wrong.
* Add documentation.

I believe this library is stable now. Someday it will turn into 1.0.0.

Version 0.1.1
~~~~~~~~~~~~~

Released on Jul 4, 2013

* Remove ``===`` for Google Authenticator. `#1`_

.. _`#1`: https://github.com/lepture/otpauth/pull/1

Version 0.1.0
~~~~~~~~~~~~~

First preview release.
