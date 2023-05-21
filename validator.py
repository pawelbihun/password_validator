"""Main modul for validating passwords"""
from abc import ABC, abstractmethod


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


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharacterValidator
        ]

    def is_valid(self):
        validation_list = []
        for class_name in self.validators:
            validator = class_name(self.password)
            validation_list.append(validator.is_valid())
        return all(validation_list)


if __name__ == '__main__':
    silly_password = 'qwerty123!'
    my_validator = PasswordValidator(silly_password)
    print(my_validator.is_valid())
