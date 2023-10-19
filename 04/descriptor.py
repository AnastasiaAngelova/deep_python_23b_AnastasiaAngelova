"""
Descriptors are implemented for the user's bank account
-Phone_number phone number of the form "+7(***)***-**-**-**"
-Balance account balance (int or float) not less than 0
-Password 8-16 characters long, containing letters, numbers and symbols
"""

import re


class Balance:
    def __set_name__(self, owner, name):
        self.name = f"login_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None

        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val,  (int, float)):
            raise TypeError("int or float required")

        if val < 0:
            raise ValueError("balance must be non-negative")

        return setattr(obj, self.name, val)


class Password:
    def __set_name__(self, owner, name):
        self.name = f"password_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None

        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val,  str):
            raise TypeError("str required")

        if len(val) < 8:
            raise ValueError("password too short: need 8-16 symbols")
        if len(val) > 16:
            raise ValueError("password too long: need 8-16 symbols")

        pattern_digits = r".*\d.*"
        if not bool(re.match(pattern_digits, val)):
            raise ValueError("password must have digits")
        pattern_letters = r".*[A-Za-z].*"
        if not bool(re.match(pattern_letters, val)):
            raise ValueError("password must have letters")
        pattern_symbols = r".*[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~].*"
        if not bool(re.match(pattern_symbols, val)):
            raise ValueError("password must have symbols")

        return setattr(obj, self.name, val)


class PhoneNumber:
    def __set_name__(self, owner, name):
        self.name = f"phone_number_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            return None

        return getattr(obj, self.name)

    def __set__(self, obj, val):
        if not isinstance(val, str):
            raise TypeError("str required")

        pattern = r'\+\d\(\d{3}\)\d{3}-\d{2}-\d{2}'
        if not re.match(pattern, val):
            raise ValueError("invalid phone number, need '+7(***)***-**-**'")

        return setattr(obj, self.name, val)


class BankAccount:
    phone_number = PhoneNumber()
    password = Password()
    balance = Balance()

    def __init__(self, phone_number, password, balance):
        self.phone_number = phone_number
        self.password = password
        self.balance = balance
