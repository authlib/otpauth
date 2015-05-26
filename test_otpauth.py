# -*- coding: utf-8 -*-
from otpauth import OtpAuth
from nose.tools import raises


def test_hotp():
    auth = OtpAuth('python')
    code = auth.hotp(4)
    assert auth.valid_hotp(code) == 4

    # false
    assert auth.valid_hotp(1234567) is False
    assert auth.valid_hotp(123456) is False
    assert auth.valid_hotp('123456') is False


def test_totp():
    auth = OtpAuth('python')
    code = auth.totp()
    assert auth.valid_totp(code)

    # false
    assert auth.valid_totp(1234567) is False
    assert auth.valid_totp(123456) is False


@raises(ValueError)
def test_to_google_raise():
    auth = OtpAuth('python')
    auth.to_google('invalid', 'python', 'python')


@raises(ValueError)
def test_to_google_hotp_raise():
    auth = OtpAuth('python')
    auth.to_google('hotp', 'python', 'python')


def test_to_google_hotp():
    auth = OtpAuth('python')
    expect = 'otpauth://hotp/python?secret=OB4XI2DPNY&issuer=python&counter=4'
    assert auth.to_google('hotp', 'python', 'python', 4) == expect


def test_to_google_totp():
    auth = OtpAuth('python')
    expect = 'otpauth://totp/python?secret=OB4XI2DPNY&issuer=python'
    assert auth.to_google('totp', 'python', 'python') == expect
