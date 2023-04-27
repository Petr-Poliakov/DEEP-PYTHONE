
class InvalidDateFormat(Exception):
    """Raised when the input date is not in the correct format DD.MM.YYYY"""
    pass


class InvalidDate(Exception):
    """Raised when the input date does not exist in the Gregorian calendar"""
    pass


class DateValidator:
    @staticmethod
    def is_leap_year(year):
        """ Check if the input year is a leap year"""
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    @staticmethod
    def is_valid_date(date_str):
        """ Check if the input date is a valid date in the Gregorian calendar"""
        try:
            day, month, year = map(int, date_str.split('.'))
        except ValueError:
            raise InvalidDateFormat('Invalid date format. Date must be in DD.MM.YYYY format')
        if month < 1 or month > 12:
            raise InvalidDate('Invalid month')
        if year < 1 or year > 9999:
            raise InvalidDate('Invalid year')
        last_day_of_month = 31
        if month == 2:
            if DateValidator.is_leap_year(year):
                last_day_of_month = 29
            else:
                last_day_of_month = 28
        elif month in [4, 6, 9, 11]:
            last_day_of_month = 30
        if day < 1 or day > last_day_of_month:
            raise InvalidDate('Invalid day')
        return True