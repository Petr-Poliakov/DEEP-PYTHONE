"""
2. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
import datetime
import calendar

def chek_date(my_date: datetime) -> bool:
    MAX_DATE = datetime.date(9999, 12, 31)
    MIN_DATE = datetime.date(1, 1, 1)
    if MIN_DATE < my_date < MAX_DATE:
        return True
    else:
        return False


def _vis_year(year: datetime):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print("Год высокостный ")
    else:
        print("Год не высокостный")
    return None


# year = a.year
# print(year)


a = datetime.date(2021, 3, 28)

print(chek_date(a))
print(_vis_year(a.year))
    