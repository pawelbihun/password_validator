"""Tests of Validators"""

from validator import PasswordValidator, LengthValidator, HasNumberValidator, HasSpecialCharacterValidator, \
    HasUpperCaseValidator, HasLowerCaseValidator, HaveIbeenPwndValidator


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


def test_has_number_validator_no_number():
    passwd = 'abc'
    validator = HasNumberValidator(passwd)
    assert validator.is_valid() is False


def test_has_number_validator_with_number():
    passwd = 'abc0'
    validator = HasNumberValidator(passwd)
    assert validator.is_valid() is True


def test_has_special_character_validator_no_special_char():
    passwd = 'abc'
    validator = HasSpecialCharacterValidator(passwd)
    assert validator.is_valid() is False


def test_has_special_character_validator_special_char():
    passwd = 'abc|'
    validator = HasSpecialCharacterValidator(passwd)
    assert validator.is_valid() is True


def test_has_uppercase_validator_no_uppercase():
    passwd = 'abc'
    validator = HasUpperCaseValidator(passwd)
    assert validator.is_valid() is False


def test_has_uppercase_validator_with_uppercase():
    passwd = 'abcD'
    validator = HasUpperCaseValidator(passwd)
    assert validator.is_valid() is True


def test_has_lowercase_validator_no_lowercase():
    passwd = 'ABCD'
    validator = HasLowerCaseValidator(passwd)
    assert validator.is_valid() is False


def test_has_lowercase_validator_with_lowercase():
    passwd = 'ABCd'
    validator = HasLowerCaseValidator(passwd)
    assert validator.is_valid() is True

def test_have_i_been_pwnd_validator():
    passwd = 'qwerty123'
    validator = HaveIbeenPwndValidator(passwd)
    assert validator.hash is None
    assert validator.hash_prefix is None
    assert validator.text == passwd
    assert validator.compromised_list == []


def test_have_i_been_pwnd_validator_get_hash():
    passwd = 'qwerty123'
    validator = HaveIbeenPwndValidator(passwd)
    validator.get_hash()
    assert validator.hash == '5CEC175B165E3D5E62C9E13CE848EF6FEAC81BFF'


def test_have_i_been_pwnd_validator_get_hash_prefix():
    passwd = 'qwerty123'
    validator = HaveIbeenPwndValidator(passwd)
    validator.get_hash()
    validator.get_hash_prefix()
    assert validator.hash_prefix == '5CEC1'
