"""Tests of Validators"""

from validator import PasswordValidator, LengthValidator


def test_password_validator_constructor():
    passwd = 'qwerty'
    validator = PasswordValidator(passwd)
    assert validator.password == 'qwerty'

def test_length_validator_has_7_char():
    passwd = 'qwerty'
    validator = LengthValidator(passwd)
    assert validator.is_valid() is False


def test_length_validator_has_8_char():
    passwd = 'qwertyui'
    validator = LengthValidator(passwd)
    assert validator.is_valid() is True
