def is_leap_year(year):
    """
    Check if a year is a leap year.

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2021)
    False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_date(date):
    """
    Check if a date in the format DD.MM.YYYY is valid.

    >>> is_valid_date('29.02.2024')
    True
    >>> is_valid_date('29.02.2023')
    False
    >>> is_valid_date('31.04.2023')
    False
    >>> is_valid_date('32.12.2023')
    False
    """
    try:
        day, month, year = map(int, date.split('.'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2 and (day > 29 or (day == 29 and not is_leap_year(year))):
            return False
        if month == 2 and day > 28 and not is_leap_year(year):
            return False
        if year < 1 or year > 9999:
            return False
        return True
    except ValueError:
        return False
