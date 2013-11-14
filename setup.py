#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # for `python setup.py test`
    import multiprocessing
except ImportError:
    pass

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import otpauth
from email.utils import parseaddr
author, author_email = parseaddr(otpauth.__author__)


def fread(path):
    with open(path, 'r') as f:
        return f.read()


setup(
    name='otpauth',
    version=otpauth.__version__,
    author=author,
    author_email=author_email,
    url=otpauth.__homepage__,
    py_modules=['otpauth'],
    description='Implements two-step verification of HOTP/TOTP',
    long_description=fread('README.rst'),
    license='BSD',
    platforms='any',
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
