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
    def __init__(self, text):
        pass

    def is_valid(self):
        pass


