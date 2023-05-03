import logging
import argparse

logging.basicConfig(filename='date_validator.log', level=logging.ERROR)

class InvalidDateFormatError(Exception):
    pass

class InvalidDateError(Exception):
    pass

def is_leap_year(year):
    """Determine whether a year is a leap year."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def is_valid_date(date_str):
    """Check if the input date is valid in the format of DD.MM.YYYY"""
    try:
        day, month, year = map(int, date_str.split('.'))
        if day < 1 or day > 31:
            raise InvalidDateError('Invalid day')
        if month < 1 or month > 12:
            raise InvalidDateError('Invalid month')
        if year < 1 or year > 9999:
            raise InvalidDateError('Invalid year')
        if month in [4, 6, 9, 11] and day == 31:
            raise InvalidDateError('Invalid day for the given month')
        if month == 2 and (day > 29 or (day == 29 and not is_leap_year(year))):
            raise InvalidDateError('Invalid day for February of the given year')
        return True
    except ValueError:
        raise InvalidDateFormatError('Invalid date format')
    except InvalidDateError as e:
        logging.error(f'Invalid date: {date_str}, error: {str(e)}')
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Date Validator')
    parser.add_argument('date', help='Input date in the format of DD.MM.YYYY')
    args = parser.parse_args()
    date_str = args.date
    try:
        if is_valid_date(date_str):
            print(f'{date_str} is a valid date.')
        else:
            print(f'{date_str} is an invalid date.')
    except (InvalidDateFormatError, InvalidDateError) as e:
        print(f'Error: {str(e)}')



date_validator.py(29.04.2023)
