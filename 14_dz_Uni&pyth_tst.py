import unittest
import date_validator

class TestDateValidator(unittest.TestCase):

    def test_is_leap_year(self):
        self.assertEqual(date_validator.is_leap_year(2000), True)
        self.assertEqual(date_validator.is_leap_year(1900), False)
        self.assertEqual(date_validator.is_leap_year(2024), True)
        self.assertEqual(date_validator.is_leap_year(2021), False)

    def test_is_valid_date(self):
        self.assertEqual(date_validator.is_valid_date('29.02.2024'), True)
        self.assertEqual(date_validator.is_valid_date('29.02.2023'), False)
        self.assertEqual(date_validator.is_valid_date('31.04.2023'), False)
        self.assertEqual(date_validator.is_valid_date('32.12.2023'), False)


import pytest
import date_validator

def test_is_leap_year():
    assert date_validator.is_leap_year(2000) == True
    assert date_validator.is_leap_year(1900) == False
    assert date_validator.is_leap_year(2024) == True
    assert date_validator.is_leap_year(2021) == False

def test_is_valid