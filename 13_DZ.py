

# Для проверки даты используется статический метод `is_valid_date`, который принимает строку с датой в формате `DD.MM.YYYY`.
# Если дата введена некорректно (например, неверный формат или неправильное значение дня, месяца и т.д.), функция выбрасывает
# соответствующее исключение.
# Для проверки на високосный год используется вспомогательный метод `is_leap_year`.
#
# Пример использования модуля:

from _class_for_DZ_13 import DateValidator, InvalidDateFormat, InvalidDate

try:
    DateValidator.is_valid_date('29.02.2021')
except InvalidDateFormat as e:
    print(e)
except InvalidDate as e:
    print(e)

try:
    DateValidator.is_valid_date('29.02.2024')
except InvalidDateFormat as e:
    print(e)
except InvalidDate as e:
    print(e)


# В первом случае мы попытались проверить некорректную дату, и `is_valid_date` выбросит исключение `InvalidDate`,
# так как 29 февраля 2021 года не существует. Во втором случае мы проверяем правильный високосный год, и функция
# ничего не выбросит.