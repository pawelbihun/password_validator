"""Main modul for validating passwords"""
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            LengthValidator
        ]

    def is_valid(self):
        validation_list = []
        for class_name in self.validators:
            validator = class_name(self.password)
            validation_list.append(validator.is_valid())
        return all(validation_list)


if __name__ == '__main__':
    silly_password = 'qwerty123'
    my_validator = PasswordValidator(silly_password)
    print(my_validator.is_valid())
