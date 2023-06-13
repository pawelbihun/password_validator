"""Main modul for validating passwords"""
import logging
from abc import ABC, abstractmethod
from hashlib import sha1
from functools import cache
from json import JSONDecodeError
from requests import get


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class LengthValidator(Validator):

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if len(self.text) >= 8:
            return True
        return False


class HasNumberValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        numbers = [str(i) for i in range(0, 10)]
        for char in self.text:
            if char in numbers:
                return True
        return False


class HasSpecialCharacterValidator(Validator):
    """Special chars have taken from https://owasp.org/www-community/password-special-characters"""

    def __init__(self, text):
        self.text = text

    def is_valid(self):
        special_chars = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for char in self.text:
            if char in special_chars:
                return True
        return False


class HasUpperCaseValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        for char in self.text:
            if char.isupper():
                return True
        return False


class HasLowerCaseValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        for char in self.text:
            if char.islower():
                return True
        return False


class HaveIbeenPwndValidator(Validator):
    def __init__(self, text):
        self.url = "https://api.pwnedpasswords.com/range/"
        self.hash_prefix = None
        self.hash = None
        self.compromised_list = []
        self.text = text

    def get_hash(self):
        self.hash = sha1(self.text.encode()).hexdigest().upper()

    def get_hash_prefix(self):
        try:
            if self.hash is not None:
                self.hash_prefix = self.hash[:5]
        except TypeError:
            logging.ERROR('Hasn\'t hash set')

    @cache
    def get_compromised_passwords(self):
        try:
            with get(f"{self.url}{self.hash_prefix}") as res:
                self.compromised_list = res.text.splitlines()

        except JSONDecodeError:
            logging.error("Encode request!")

    def is_valid(self):
        self.get_hash()
        self.get_hash_prefix()
        self.get_compromised_passwords()
        for line in self.compromised_list:
            if line.split(':')[0] == self.hash[5:]:
                return False

        return True


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharacterValidator,
            HasUpperCaseValidator,
            HasLowerCaseValidator,
            HaveIbeenPwndValidator
        ]

    def is_valid(self):
        validation_list = []
        for class_name in self.validators:
            print(f'{class_name} is valid: ', end='')
            validator = class_name(self.password)
            is_valid = validator.is_valid()
            print(is_valid)
            validation_list.append(is_valid)
        return all(validation_list)


if __name__ == '__main__':
    password = 'Qwerty1!'
    my_validator = PasswordValidator(password)
    print(my_validator.is_valid())
