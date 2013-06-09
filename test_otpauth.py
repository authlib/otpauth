from otpauth import OtpAuth


def test_hotp():
    auth = OtpAuth('python')
    code = auth.hotp(4)
    assert auth.valid_hotp(code) == 4


def test_totp():
    auth = OtpAuth('python')
    code = auth.totp()
    assert auth.valid_totp(code)
